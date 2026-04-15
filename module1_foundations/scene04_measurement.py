"""1.4 — Measurement (animation only)"""
from manim import *
import numpy as np
import random
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QORANGE
from common.quantum import BlochSphere


class MeasurementScene(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        # ── Bloch sphere in superposition → measurement collapse ──
        bloch = BlochSphere(radius=1.5, theta=np.pi / 2, phi=0)
        bloch.move_to(LEFT * 3)

        state_lbl = MathTex(
            r"\tfrac{1}{\sqrt{2}}(|0\rangle + |1\rangle)", font_size=30, color=QWHITE,
        ).next_to(bloch, UP, buff=0.4)

        self.play(FadeIn(bloch, scale=0.8), Write(state_lbl))
        self.wait(1)

        # Measurement icon
        meter = VGroup(
            RoundedRectangle(width=1.8, height=1.4, corner_radius=0.15, color=QGREEN, fill_opacity=0.15),
            Arc(radius=0.4, start_angle=PI, angle=-PI, color=QGREEN, stroke_width=3).shift(0.1 * DOWN),
            Line(0.1 * DOWN, 0.4 * UP + 0.3 * RIGHT, color=QGREEN, stroke_width=3),
        ).move_to(RIGHT * 0.5)

        arrow_in = Arrow(bloch.get_right(), meter.get_left(), color=QGRAY, buff=0.3)
        self.play(GrowArrow(arrow_in), FadeIn(meter))
        self.wait(0.5)

        # Flash → collapse
        flash = Circle(radius=0.01, color=QGREEN, fill_opacity=1).move_to(meter)
        self.play(flash.animate.scale(80).set_opacity(0), run_time=0.4)

        result = MathTex(r"|0\rangle", font_size=52, color=QBLUE).move_to(RIGHT * 3.5)
        arrow_out = Arrow(meter.get_right(), result.get_left(), color=QGRAY, buff=0.3)
        self.play(GrowArrow(arrow_out), Write(result))
        self.play(
            bloch.animate_to_state(0, 0),
            Transform(state_lbl, MathTex(r"|0\rangle", font_size=30, color=QBLUE).next_to(bloch, UP, buff=0.4)),
            run_time=1,
        )
        self.wait(1.5)

        self.play(
            FadeOut(bloch), FadeOut(state_lbl), FadeOut(arrow_in),
            FadeOut(meter), FadeOut(arrow_out), FadeOut(result),
        )

        # ── Repeated measurements histogram ──────────────────
        random.seed(42)
        count_0, count_1 = 0, 0
        num_shots = 40
        bar_max_h = 3.0

        bar_0 = Rectangle(width=1.0, height=0.01, fill_color=QBLUE, fill_opacity=0.8, stroke_width=0)
        bar_1 = Rectangle(width=1.0, height=0.01, fill_color=QRED, fill_opacity=0.8, stroke_width=0)
        bar_0.align_to(1.5 * DOWN, DOWN).shift(1.5 * LEFT)
        bar_1.align_to(1.5 * DOWN, DOWN).shift(1.5 * RIGHT)

        lbl_0 = MathTex(r"|0\rangle", font_size=28, color=QBLUE).next_to(bar_0, DOWN, buff=0.15)
        lbl_1 = MathTex(r"|1\rangle", font_size=28, color=QRED).next_to(bar_1, DOWN, buff=0.15)
        count_lbl_0 = Text("0", font_size=24, color=QWHITE).next_to(bar_0, UP, buff=0.1)
        count_lbl_1 = Text("0", font_size=24, color=QWHITE).next_to(bar_1, UP, buff=0.1)

        self.play(FadeIn(bar_0), FadeIn(bar_1), FadeIn(lbl_0), FadeIn(lbl_1))
        self.add(count_lbl_0, count_lbl_1)

        for _ in range(num_shots):
            if random.random() < 0.5:
                count_0 += 1
            else:
                count_1 += 1
            h0 = max(bar_max_h * count_0 / num_shots, 0.01)
            h1 = max(bar_max_h * count_1 / num_shots, 0.01)
            new_b0 = Rectangle(width=1.0, height=h0, fill_color=QBLUE, fill_opacity=0.8, stroke_width=0)
            new_b0.align_to(1.5 * DOWN, DOWN).shift(1.5 * LEFT)
            new_b1 = Rectangle(width=1.0, height=h1, fill_color=QRED, fill_opacity=0.8, stroke_width=0)
            new_b1.align_to(1.5 * DOWN, DOWN).shift(1.5 * RIGHT)
            new_c0 = Text(str(count_0), font_size=24, color=QWHITE).next_to(new_b0, UP, buff=0.1)
            new_c1 = Text(str(count_1), font_size=24, color=QWHITE).next_to(new_b1, UP, buff=0.1)
            self.play(
                Transform(bar_0, new_b0), Transform(bar_1, new_b1),
                Transform(count_lbl_0, new_c0), Transform(count_lbl_1, new_c1),
                run_time=0.08, rate_func=linear,
            )

        self.wait(2)
        self.play(FadeOut(bar_0), FadeOut(bar_1), FadeOut(lbl_0), FadeOut(lbl_1),
                  FadeOut(count_lbl_0), FadeOut(count_lbl_1))
