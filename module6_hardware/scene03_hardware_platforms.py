"""5.3 — Quantum Hardware Platforms (animation only)"""
from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QPURPLE, QORANGE, QCYAN


class HardwarePlatformsScene(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        # ── Superconducting Qubits ────────────────────────────
        self._show_platform(
            name="Superconducting",
            icon_color=QBLUE,
            stats=[
                ("Gate speed", "~20 ns"),
                ("Coherence", "~100 μs"),
                ("Qubits", "1,000+"),
                ("Connectivity", "Nearest-neighbor"),
            ],
            chip_func=self._draw_superconducting,
        )

        # ── Trapped Ions ──────────────────────────────────────
        self._show_platform(
            name="Trapped Ions",
            icon_color=QPURPLE,
            stats=[
                ("Gate speed", "~1–100 μs"),
                ("Coherence", "seconds–minutes"),
                ("Fidelity", ">99.9%"),
                ("Connectivity", "All-to-all"),
            ],
            chip_func=self._draw_trapped_ions,
        )

        # ── Photonic ──────────────────────────────────────────
        self._show_platform(
            name="Photonic",
            icon_color=QGREEN,
            stats=[
                ("Temp", "Room temperature"),
                ("Qubit", "Photons"),
                ("Strength", "Networking"),
                ("Challenge", "2-qubit gates"),
            ],
            chip_func=self._draw_photonic,
        )

        # ── Comparison table with proper grid ─────────────────
        col_widths = [1.8, 1.4, 1.6, 1.4]
        row_height = 0.55
        headers = ["Platform", "Speed", "Coherence", "Scale"]
        data = [
            ("Superconducting", "20 ns", "100 μs", "1000+"),
            ("Trapped Ions", "1 μs", "minutes", "~50"),
            ("Photonic", "ps", "long", "~200"),
        ]
        row_colors = [QBLUE, QPURPLE, QGREEN]
        n_rows = len(data) + 1
        n_cols = len(headers)
        total_w = sum(col_widths)
        total_h = n_rows * row_height

        table_group = VGroup()
        table_origin = np.array([-total_w / 2, total_h / 2, 0])

        # Horizontal lines
        for r in range(n_rows + 1):
            y = table_origin[1] - r * row_height
            start = np.array([table_origin[0], y, 0])
            end = np.array([table_origin[0] + total_w, y, 0])
            weight = 2.5 if r <= 1 else 1.5
            color = QWHITE if r == 0 or r == 1 else QGRAY
            line = Line(start, end, color=color, stroke_width=weight, stroke_opacity=0.6)
            table_group.add(line)

        # Vertical lines
        x_offset = table_origin[0]
        for c in range(n_cols + 1):
            x = x_offset
            start = np.array([x, table_origin[1], 0])
            end = np.array([x, table_origin[1] - total_h, 0])
            line = Line(start, end, color=QGRAY, stroke_width=1.5, stroke_opacity=0.5)
            table_group.add(line)
            if c < n_cols:
                x_offset += col_widths[c]

        # Header text
        x_pos = table_origin[0]
        for c, h in enumerate(headers):
            cx = x_pos + col_widths[c] / 2
            cy = table_origin[1] - row_height / 2
            txt = Text(h, font_size=18, color=QWHITE, weight=BOLD)
            txt.move_to(np.array([cx, cy, 0]))
            table_group.add(txt)
            x_pos += col_widths[c]

        # Data rows
        for r, ((name, speed, coh, scale), color) in enumerate(zip(data, row_colors)):
            x_pos = table_origin[0]
            cy = table_origin[1] - (r + 1.5) * row_height
            cells_data = [
                (name, color),
                (speed, QWHITE),
                (coh, QWHITE),
                (scale, QWHITE),
            ]
            for c, (val, clr) in enumerate(cells_data):
                cx = x_pos + col_widths[c] / 2
                txt = Text(val, font_size=16, color=clr)
                txt.move_to(np.array([cx, cy, 0]))
                table_group.add(txt)
                x_pos += col_widths[c]

        self.play(FadeIn(table_group, shift=UP * 0.3), run_time=1.5)
        self.wait(3)
        self.play(FadeOut(table_group))

    def _show_platform(self, name, icon_color, stats, chip_func):
        title = Text(name, font_size=34, color=icon_color, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        # Draw visual on the left
        visual = chip_func()
        visual.move_to(LEFT * 3)
        self.play(FadeIn(visual, scale=0.8))

        # Stats on the right
        stat_group = VGroup()
        for label, value in stats:
            row = VGroup(
                Text(f"{label}:", font_size=20, color=QGRAY),
                Text(value, font_size=20, color=QWHITE),
            ).arrange(RIGHT, buff=0.4)
            stat_group.add(row)
        stat_group.arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(RIGHT * 3)
        self.play(FadeIn(stat_group, shift=LEFT * 0.2))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(visual), FadeOut(stat_group))

    def _draw_superconducting(self):
        """Grid of qubits with nearest-neighbor connections."""
        dots = VGroup()
        lines = VGroup()
        for r in range(4):
            for c in range(4):
                pos = np.array([c * 0.6, -r * 0.6, 0])
                dots.add(Dot(pos, radius=0.12, color=QBLUE))
                if c < 3:
                    lines.add(Line(pos, pos + 0.6 * RIGHT, color=QCYAN, stroke_width=1.5, stroke_opacity=0.4))
                if r < 3:
                    lines.add(Line(pos, pos + 0.6 * DOWN, color=QCYAN, stroke_width=1.5, stroke_opacity=0.4))
        chip = RoundedRectangle(
            width=2.8, height=2.8, corner_radius=0.15,
            color=QGRAY, stroke_opacity=0.3, fill_opacity=0.05,
        ).move_to(dots.get_center())
        return VGroup(chip, lines, dots)

    def _draw_trapped_ions(self):
        """Line of ions with all-to-all connections."""
        ions = VGroup()
        positions = []
        for i in range(6):
            pos = np.array([i * 0.5 - 1.25, 0, 0])
            positions.append(pos)
            ions.add(Dot(pos, radius=0.12, color=QPURPLE))

        # All-to-all connections (curved arcs)
        connections = VGroup()
        for i in range(len(positions)):
            for j in range(i + 2, min(i + 4, len(positions))):
                mid_y = 0.2 + 0.15 * (j - i)
                arc = ArcBetweenPoints(
                    positions[i], positions[j],
                    angle=-(0.4 + 0.15 * (j - i)),
                    color=QPURPLE, stroke_width=1, stroke_opacity=0.3,
                )
                connections.add(arc)

        # Trap electrodes
        trap_top = Line(LEFT * 1.5 + UP * 0.5, RIGHT * 1.5 + UP * 0.5, color=QORANGE, stroke_width=2, stroke_opacity=0.4)
        trap_bot = Line(LEFT * 1.5 + DOWN * 0.5, RIGHT * 1.5 + DOWN * 0.5, color=QORANGE, stroke_width=2, stroke_opacity=0.4)

        return VGroup(trap_top, trap_bot, connections, ions)

    def _draw_photonic(self):
        """Beam splitters and photon paths."""
        paths = VGroup()
        splitters = VGroup()
        photons = VGroup()

        # Horizontal waveguides
        for i in range(3):
            y = -i * 0.7
            paths.add(Line(LEFT * 1.5 + y * UP, RIGHT * 1.5 + y * UP,
                           color=QGREEN, stroke_width=2, stroke_opacity=0.3))

        # Beam splitters (diagonal lines connecting paths)
        for i in range(2):
            x = -0.5 + i * 1.0
            for j in range(2):
                y_start = -j * 0.7
                y_end = -(j + 1) * 0.7
                bs = Line(
                    np.array([x, y_start, 0]), np.array([x + 0.3, y_end, 0]),
                    color=QGREEN, stroke_width=2,
                )
                splitters.add(bs)

        # Photon dots
        for i in range(3):
            y = -i * 0.7
            photons.add(Dot(LEFT * 1.2 + y * UP, radius=0.08, color=QWHITE))

        return VGroup(paths, splitters, photons)
