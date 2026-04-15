"""3.3 — Superdense Coding (animation only)"""
from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QPURPLE, QORANGE
from common.circuit import QuantumCircuit


class SuperdenseCodingScene(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        # ── Encoding table with grid lines ───────────────────
        col_widths = [1.2, 1.2, 2.2]
        row_height = 0.55
        headers = ["Message", "Gate", "Bell State"]
        data = [
            ("00", "I", r"|\Phi^+\rangle"),
            ("01", "X", r"|\Psi^+\rangle"),
            ("10", "Z", r"|\Phi^-\rangle"),
            ("11", "XZ", r"|\Psi^-\rangle"),
        ]
        n_rows = len(data) + 1  # +1 for header
        n_cols = len(headers)
        total_w = sum(col_widths)
        total_h = n_rows * row_height

        # Build the table centered at origin
        table_group = VGroup()
        table_origin = np.array([-total_w / 2, total_h / 2, 0])

        # Draw grid lines
        # Horizontal lines
        for r in range(n_rows + 1):
            y = table_origin[1] - r * row_height
            start = np.array([table_origin[0], y, 0])
            end = np.array([table_origin[0] + total_w, y, 0])
            weight = 2.5 if r <= 1 else 1.5
            color = QGRAY if r > 0 else QWHITE
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
        for r, (msg, gate, bell) in enumerate(data):
            x_pos = table_origin[0]
            cy = table_origin[1] - (r + 1.5) * row_height
            cells = [
                MathTex(msg, font_size=22, color=QWHITE),
                MathTex(gate, font_size=22, color=QORANGE),
                MathTex(bell, font_size=22, color=QPURPLE),
            ]
            for c, cell in enumerate(cells):
                cx = x_pos + col_widths[c] / 2
                cell.move_to(np.array([cx, cy, 0]))
                table_group.add(cell)
                x_pos += col_widths[c]

        self.play(FadeIn(table_group, lag_ratio=0.02), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(table_group))

        # ── Circuit (encode "01" example) ─────────────────────
        circ = QuantumCircuit(num_qubits=2, num_cols=8, wire_length=9, labels=["0", "0"])
        self.play(FadeIn(circ))

        # Bell pair
        h_g = circ.add_single_gate("H", 0, 1, color=QGREEN)
        cnot_bell = circ.add_cnot(0, 1, 2, color=QPURPLE)
        self.play(FadeIn(h_g, scale=1.2), FadeIn(cnot_bell, scale=1.2))
        circ.add_barrier(3)

        # Alice encodes 01 → X
        x_gate = circ.add_single_gate("X", 0, 4, color=QRED)
        self.play(FadeIn(x_gate, scale=1.2))
        circ.add_barrier(5)

        # Bob decodes
        cnot_dec = circ.add_cnot(0, 1, 6, color=QBLUE)
        h_dec = circ.add_single_gate("H", 0, 7, color=QBLUE)
        self.play(FadeIn(cnot_dec, scale=1.2), FadeIn(h_dec, scale=1.2))

        result = MathTex(r"\to |01\rangle", font_size=30, color=QGREEN)
        result.next_to(circ, DOWN, buff=0.6)
        self.play(Write(result))
        self.wait(2)

        self.play(FadeOut(circ), FadeOut(h_g), FadeOut(cnot_bell), FadeOut(x_gate),
                  FadeOut(cnot_dec), FadeOut(h_dec), FadeOut(result))
