"""5.1 — Quantum Noise & Decoherence (animation only)"""
from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QPURPLE, QORANGE
from common.quantum import BlochSphere


class NoiseDecoherenceScene(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        # ── T1 Relaxation: |1⟩ decays to |0⟩ ─────────────────
        bloch = BlochSphere(radius=1.5, theta=np.pi, phi=0)
        bloch.move_to(LEFT * 3)
        t1_label = MathTex(r"T_1 \text{ Relaxation}", font_size=30, color=QRED)
        t1_label.to_edge(UP, buff=0.5)
        state_lbl = MathTex(r"|1\rangle", font_size=32, color=QRED).next_to(bloch, UP, buff=0.4)

        # Energy diagram on the right
        e1_line = Line(RIGHT * 1.5 + UP * 1.5, RIGHT * 4.5 + UP * 1.5, color=QRED, stroke_width=2)
        e0_line = Line(RIGHT * 1.5 + DOWN * 1.5, RIGHT * 4.5 + DOWN * 1.5, color=QBLUE, stroke_width=2)
        e1_lbl = MathTex(r"|1\rangle", font_size=24, color=QRED).next_to(e1_line, LEFT, buff=0.2)
        e0_lbl = MathTex(r"|0\rangle", font_size=24, color=QBLUE).next_to(e0_line, LEFT, buff=0.2)
        energy_dot = Dot(RIGHT * 3 + UP * 1.5, color=QRED, radius=0.12)
        decay_arrow = Arrow(RIGHT * 3 + UP * 1.2, RIGHT * 3 + DOWN * 1.2,
                            color=QORANGE, stroke_width=3, buff=0.1)
        decay_lbl = MathTex(r"\gamma", font_size=22, color=QORANGE).next_to(decay_arrow, RIGHT, buff=0.15)

        self.play(Write(t1_label), FadeIn(bloch, scale=0.8), Write(state_lbl))
        self.play(FadeIn(e1_line), FadeIn(e0_line), Write(e1_lbl), Write(e0_lbl),
                  FadeIn(energy_dot))
        self.wait(0.5)
        self.play(GrowArrow(decay_arrow), Write(decay_lbl))

        # Bloch sphere: |1⟩ → |0⟩ slowly
        steps = 20
        for i in range(1, steps + 1):
            theta = np.pi * (1 - i / steps)
            self.play(
                bloch.animate_to_state(theta, 0),
                energy_dot.animate.move_to(RIGHT * 3 + UP * 1.5 * (1 - 2 * i / steps)),
                run_time=0.12, rate_func=linear,
            )
        new_lbl = MathTex(r"|0\rangle", font_size=32, color=QBLUE).next_to(bloch, UP, buff=0.4)
        self.play(Transform(state_lbl, new_lbl))
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ── T2 Dephasing: phase randomizes ───────────────────
        bloch2 = BlochSphere(radius=1.5, theta=np.pi / 2, phi=0)
        bloch2.move_to(LEFT * 2)
        t2_label = MathTex(r"T_2 \text{ Dephasing}", font_size=30, color=QPURPLE)
        t2_label.to_edge(UP, buff=0.5)

        phase_lbl = MathTex(r"|+\rangle", font_size=32, color=QGREEN).next_to(bloch2, UP, buff=0.4)
        self.play(Write(t2_label), FadeIn(bloch2, scale=0.8), Write(phase_lbl))
        self.wait(0.5)

        # Phase spirals randomly and amplitude shrinks on equator
        rng = np.random.default_rng(42)
        phi = 0.0
        for i in range(30):
            phi += rng.uniform(-0.5, 0.5)
            # Gradually move theta toward 0 (mixed state → north pole in Bloch picture)
            theta_now = np.pi / 2
            self.play(bloch2.animate_to_state(theta_now, phi), run_time=0.1, rate_func=linear)

        # Show arrow shrinking (decoherence)
        for i in range(10):
            scale_factor = 1 - (i + 1) * 0.08
            self.play(
                bloch2.state_arrow.animate.scale(scale_factor, about_point=bloch2.get_center()),
                bloch2.state_dot.animate.scale(scale_factor),
                run_time=0.1, rate_func=linear,
            )

        mixed_lbl = MathTex(r"\text{mixed state}", font_size=26, color=QGRAY).next_to(bloch2, UP, buff=0.4)
        self.play(Transform(phase_lbl, mixed_lbl))
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ── Noise models comparison bars ──────────────────────
        models = [
            ("Bit Flip", r"X", QRED),
            ("Phase Flip", r"Z", QBLUE),
            ("Depolarizing", r"X,Y,Z", QPURPLE),
            ("Amp. Damping", r"|1\rangle\!\to\!|0\rangle", QORANGE),
        ]
        boxes = VGroup()
        for name, sym, color in models:
            box = VGroup(
                RoundedRectangle(width=2.4, height=1.6, corner_radius=0.12,
                                 color=color, fill_opacity=0.15, stroke_width=2),
                Text(name, font_size=18, color=color, weight=BOLD).shift(UP * 0.35),
                MathTex(sym, font_size=22, color=QWHITE).shift(DOWN * 0.25),
            )
            boxes.add(box)
        boxes.arrange(RIGHT, buff=0.4)

        for box in boxes:
            self.play(FadeIn(box, shift=UP * 0.2), run_time=0.5)
        self.wait(2)
        self.play(FadeOut(boxes))

        # ── Gate fidelity timeline ────────────────────────────
        fid_title = MathTex(r"\text{Gate Fidelity}", font_size=30, color=QGREEN)
        fid_title.to_edge(UP, buff=0.5)
        self.play(Write(fid_title))

        # Show accumulated error
        fidelities = [0.995 ** n for n in range(1, 51)]
        axes_o = LEFT * 5 + DOWN * 1.0
        x_ax = Arrow(axes_o, axes_o + 10 * RIGHT, color=QGRAY, buff=0, stroke_width=2)
        y_ax = Arrow(axes_o, axes_o + 3 * UP, color=QGRAY, buff=0, stroke_width=2)
        x_lbl = MathTex(r"\text{gates}", font_size=18, color=QGRAY).next_to(x_ax, DOWN, buff=0.1)
        y_lbl = MathTex(r"\text{fidelity}", font_size=18, color=QGRAY).next_to(y_ax, LEFT, buff=0.1)
        self.play(GrowArrow(x_ax), GrowArrow(y_ax), Write(x_lbl), Write(y_lbl))

        dx = 10 / 50
        dy = 2.8
        dots = VGroup()
        for i, f in enumerate(fidelities):
            pos = axes_o + (i + 1) * dx * RIGHT + f * dy * UP
            dot = Dot(pos, radius=0.04, color=QGREEN)
            dots.add(dot)

        self.play(FadeIn(dots, lag_ratio=0.05), run_time=2)

        # Dashed line at 50%
        half_line = DashedLine(
            axes_o + 0.5 * dy * UP, axes_o + 10 * RIGHT + 0.5 * dy * UP,
            color=QRED, stroke_opacity=0.5, stroke_width=1.5,
        )
        half_lbl = MathTex(r"50\%", font_size=18, color=QRED).next_to(half_line, RIGHT, buff=0.15)
        self.play(Create(half_line), Write(half_lbl))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])
