"""1.4 - Measurement

Teaching objective: show how measurement collapses a superposition to
a definite outcome and how repeated measurements produce a probability
histogram that approximates Born-rule probabilities.
"""
from manim import *
import numpy as np
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QWHITE, QGRAY, QGREEN, QORANGE,
    STEP_PAUSE, LONG_PAUSE,
)
from common.quantum import BlochSphere

# -- Layout constants --
SPHERE_CENTER = np.array([-3.8, -0.3, 0])
SPHERE_RADIUS = 1.3
EQ_POS = np.array([-3.8, 2.8, 0])
METER_X = 0.0
RESULT_X = 3.5

# R4b: histogram constants
HIST_BASELINE_Y = -1.5
HIST_LABEL_Y = HIST_BASELINE_Y - 0.35
HIST_BAR_MAX_H = 3.0
HIST_BAR_W = 1.0
HIST_X0, HIST_X1 = -1.5, 1.5


def _hist_bar(count, total, color, cx):
    h = max(HIST_BAR_MAX_H * count / total, 0.01)
    bar = Rectangle(
        width=HIST_BAR_W, height=h,
        fill_color=color, fill_opacity=0.8, stroke_width=0,
    )
    bar.move_to(np.array([cx, HIST_BASELINE_Y + h / 2, 0]))
    return bar


class MeasurementScene(QScene):
    """Scene 1.4 - Measurement."""

    def construct(self):
        self.show_title_card("Measurement")

        # -- Beat 2: Bloch sphere in |+> --
        sec = self.show_section("Collapse", QGREEN)

        bloch = BlochSphere(radius=SPHERE_RADIUS, theta=np.pi / 2, phi=0)
        bloch.move_to(SPHERE_CENTER)

        state_lbl = MathTex(
            r"|\psi\rangle = \tfrac{1}{\sqrt{2}}(|0\rangle + |1\rangle)",
            font_size=24, color=QWHITE,
        ).move_to(EQ_POS)

        self.play(FadeIn(bloch, scale=0.85), Write(state_lbl))
        self.pause()

        # -- Beat 3: Measurement collapse --
        meter = VGroup(
            RoundedRectangle(
                width=1.5, height=1.1, corner_radius=0.12,
                color=QGREEN, fill_opacity=0.15,
            ),
            Arc(
                radius=0.3, start_angle=PI, angle=-PI,
                color=QGREEN, stroke_width=3,
            ).shift(0.06 * DOWN),
            Line(
                0.06 * DOWN, 0.3 * UP + 0.2 * RIGHT,
                color=QGREEN, stroke_width=3,
            ),
        ).move_to(np.array([METER_X, SPHERE_CENTER[1], 0]))

        arrow_in = Arrow(
            bloch.get_right(), meter.get_left(),
            color=QGRAY, buff=0.15, stroke_width=3,
        )
        self.play(GrowArrow(arrow_in), FadeIn(meter))
        self.wait(0.5)

        flash = Circle(
            radius=0.01, color=QGREEN, fill_opacity=1,
        ).move_to(meter)
        self.play(flash.animate.scale(80).set_opacity(0), run_time=0.4)

        result = MathTex(
            r"|0\rangle", font_size=52, color=QBLUE,
        ).move_to(np.array([RESULT_X, SPHERE_CENTER[1], 0]))
        arrow_out = Arrow(
            meter.get_right(), result.get_left(),
            color=QGRAY, buff=0.15, stroke_width=3,
        )
        self.play(GrowArrow(arrow_out), Write(result))

        collapsed_lbl = MathTex(
            r"|\psi\rangle = |0\rangle \;\;\text{(collapsed)}",
            font_size=24, color=QBLUE,
        ).move_to(EQ_POS)

        irreversible = Text(
            "irreversible", font_size=22, color=QRED,
        ).next_to(collapsed_lbl, DOWN, buff=0.15)

        self.play(
            bloch.animate_to_state(0, 0),
            Transform(state_lbl, collapsed_lbl),
            run_time=1.5,
        )
        self.play(FadeIn(irreversible, shift=DOWN * 0.2))
        self.play(Indicate(irreversible, color=QRED, scale_factor=1.3))
        self.wait(LONG_PAUSE)
        self.fade_out_group(
            bloch, state_lbl, irreversible,
            arrow_in, meter, arrow_out, result, sec,
        )

        # -- Beat 4/5: Repeated-measurement histogram --
        sec2 = self.show_section("Statistics", QORANGE)

        random.seed(42)
        count_0, count_1 = 0, 0
        num_shots = 40

        bar_0 = Rectangle(
            width=HIST_BAR_W, height=0.01,
            fill_color=QBLUE, fill_opacity=0.8, stroke_width=0,
        ).move_to(np.array([HIST_X0, HIST_BASELINE_Y, 0]), aligned_edge=DOWN)
        bar_1 = Rectangle(
            width=HIST_BAR_W, height=0.01,
            fill_color=QRED, fill_opacity=0.8, stroke_width=0,
        ).move_to(np.array([HIST_X1, HIST_BASELINE_Y, 0]), aligned_edge=DOWN)

        lbl_0 = MathTex(
            r"|0\rangle", font_size=28, color=QBLUE,
        ).move_to(np.array([HIST_X0, HIST_LABEL_Y, 0]))
        lbl_1 = MathTex(
            r"|1\rangle", font_size=28, color=QRED,
        ).move_to(np.array([HIST_X1, HIST_LABEL_Y, 0]))

        cnt_0 = Text("0", font_size=24, color=QWHITE).next_to(bar_0, UP, buff=0.1)
        cnt_1 = Text("0", font_size=24, color=QWHITE).next_to(bar_1, UP, buff=0.1)

        self.play(FadeIn(bar_0), FadeIn(bar_1), FadeIn(lbl_0, shift=UP * 0.2), FadeIn(lbl_1, shift=UP * 0.2))
        self.add(cnt_0, cnt_1)

        batch = 5
        for _ in range(0, num_shots, batch):
            for _ in range(batch):
                if random.random() < 0.5:
                    count_0 += 1
                else:
                    count_1 += 1

            nb0 = _hist_bar(count_0, num_shots, QBLUE, HIST_X0)
            nb1 = _hist_bar(count_1, num_shots, QRED, HIST_X1)
            nc0 = Text(str(count_0), font_size=24, color=QWHITE).next_to(nb0, UP, buff=0.1)
            nc1 = Text(str(count_1), font_size=24, color=QWHITE).next_to(nb1, UP, buff=0.1)

            self.play(
                Transform(bar_0, nb0), Transform(bar_1, nb1),
                Transform(cnt_0, nc0), Transform(cnt_1, nc1),
                run_time=0.5,
            )

        # -- Beat 6: Born-rule annotation --
        born = Text(
            "frequencies  ->  Born-rule  probabilities",
            font_size=24, color=QGREEN,
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(born), run_time=1.5)
        self.play(Indicate(born, color=QGREEN, scale_factor=1.1))
        self.wait(LONG_PAUSE)
        self.clear_scene()
