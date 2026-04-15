"""4.4 — Shor's Algorithm (animation only)"""
from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QPURPLE, QORANGE, QYELLOW


class ShorsAlgorithmScene(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        # ── Factoring equation ────────────────────────────────
        n_eq = MathTex(r"N = p \times q", font_size=48, color=QWHITE)
        example = MathTex(r"15 = 3 \times 5", font_size=36, color=QGRAY).next_to(n_eq, DOWN, buff=0.5)
        self.play(Write(n_eq))
        self.play(Write(example))
        self.wait(1.5)
        self.play(FadeOut(n_eq), FadeOut(example))

        # ── Period finding: f(x) = a^x mod N ─────────────────
        f_eq = MathTex(r"f(x) = a^x \bmod N", font_size=40, color=QORANGE)
        self.play(Write(f_eq))
        self.wait(1)
        self.play(f_eq.animate.scale(0.7).to_edge(UP, buff=0.5))

        # Plot f(x) = 2^x mod 15
        values = [1, 2, 4, 8, 1, 2, 4, 8, 1, 2, 4, 8]
        axes_origin = LEFT * 4.5 + DOWN * 1.5
        x_len, y_len = 9.0, 2.5

        x_axis = Arrow(axes_origin, axes_origin + x_len * RIGHT, color=QGRAY, buff=0, stroke_width=2)
        y_axis = Arrow(axes_origin, axes_origin + y_len * UP, color=QGRAY, buff=0, stroke_width=2)
        self.play(GrowArrow(x_axis), GrowArrow(y_axis))

        dx = x_len / (len(values) + 1)
        dy = y_len / 10
        dots = VGroup()
        for i, v in enumerate(values):
            pos = axes_origin + (i + 1) * dx * RIGHT + v * dy * UP
            dots.add(Dot(pos, color=QBLUE, radius=0.06))
        self.play(FadeIn(dots, lag_ratio=0.1), run_time=1.5)

        # Period bracket
        period_brace = BraceBetweenPoints(
            axes_origin + 1 * dx * RIGHT + DOWN * 0.3,
            axes_origin + 5 * dx * RIGHT + DOWN * 0.3,
            direction=DOWN, color=QORANGE,
        )
        period_lbl = MathTex(r"r = 4", font_size=28, color=QORANGE).next_to(period_brace, DOWN, buff=0.15)
        self.play(Create(period_brace), Write(period_lbl))
        self.wait(2)
        self.play(FadeOut(dots), FadeOut(x_axis), FadeOut(y_axis),
                  FadeOut(period_brace), FadeOut(period_lbl), FadeOut(f_eq))

        # ── Algorithm steps ───────────────────────────────────
        steps = VGroup()
        for num, tex, color in [
            ("1", r"\text{Choose random } a < N", QBLUE),
            ("2", r"\gcd(a, N) \neq 1 \Rightarrow \text{done}", QBLUE),
            ("3", r"\text{QFT} \to \text{find period } r", QGREEN),
            ("4", r"\text{Factors} = \gcd(a^{r/2} \pm 1, \; N)", QORANGE),
        ]:
            circle = Circle(radius=0.25, color=color, fill_opacity=0.3, stroke_width=2)
            num_lbl = Text(num, font_size=22, color=color, weight=BOLD).move_to(circle)
            txt = MathTex(tex, font_size=28, color=QWHITE)
            row = VGroup(VGroup(circle, num_lbl), txt).arrange(RIGHT, buff=0.4)
            steps.add(row)
        steps.arrange(DOWN, buff=0.4, aligned_edge=LEFT)

        for step in steps:
            self.play(FadeIn(step, shift=RIGHT * 0.3), run_time=0.8)
            self.wait(0.4)

        # Highlight quantum step
        highlight = SurroundingRectangle(steps[2], color=QGREEN, corner_radius=0.1, buff=0.1)
        self.play(Create(highlight))
        self.wait(2)
        self.play(FadeOut(steps), FadeOut(highlight))

        # ── Complexity comparison ─────────────────────────────
        impact = VGroup(
            MathTex(r"\text{Classical: } O(e^{n^{1/3}})", font_size=32, color=QRED),
            MathTex(r"\text{Quantum: } O(n^3)", font_size=32, color=QGREEN),
        ).arrange(DOWN, buff=0.5)
        self.play(Write(impact), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(impact))
