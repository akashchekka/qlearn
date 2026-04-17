"""1.1 - What Is a Qubit?

Teaching objective: contrast a classical bit (0 OR 1) with a qubit
(alpha|0> + beta|1>) and introduce the normalization constraint.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QWHITE, QGRAY, QGREEN, QPURPLE,
    STEP_PAUSE, LONG_PAUSE,
)


class WhatIsAQubit(QScene):
    def construct(self):
        self.show_title_card("What Is a Qubit?")

        # Beat 2 - Classical bit: 0 OR 1
        sec = self.show_section("Classical Bit", QGRAY)

        bit_0 = VGroup(
            Square(side_length=1.2, color=QBLUE, fill_opacity=0.3),
            Text("0", font_size=48, color=QBLUE, weight=BOLD),
        ).move_to(2 * LEFT)
        bit_1 = VGroup(
            Square(side_length=1.2, color=QRED, fill_opacity=0.3),
            Text("1", font_size=48, color=QRED, weight=BOLD),
        ).move_to(2 * RIGHT)
        or_label = Text("OR", font_size=28, color=QGRAY)

        self.play(FadeIn(bit_0, shift=LEFT * 0.3), FadeIn(bit_1, shift=RIGHT * 0.3))
        self.play(Write(or_label))
        self.pause()

        switch_arrow = Arrow(bit_0.get_right(), bit_1.get_left(), color=QGRAY, buff=0.3)
        self.play(GrowArrow(switch_arrow))
        self.pause()
        self.fade_out_group(bit_0, bit_1, or_label, switch_arrow, sec)

        # Beat 3 - Qubit: |0> AND |1>
        sec2 = self.show_section("Qubit", QBLUE)

        ket_0 = MathTex(r"|0\rangle", font_size=56, color=QBLUE).move_to(2.5 * LEFT)
        ket_1 = MathTex(r"|1\rangle", font_size=56, color=QRED).move_to(2.5 * RIGHT)
        and_label = Text("AND", font_size=28, color=QGREEN)

        self.play(Write(ket_0), Write(ket_1))
        self.play(FadeIn(and_label, scale=1.3))
        self.wait(LONG_PAUSE)
        self.fade_out_group(ket_0, ket_1, and_label, sec2)

        # Beat 4 - Superposition equation
        sec3 = self.show_section("Superposition", QPURPLE)

        superposition_eq = MathTex(
            r"|\psi\rangle", "=", r"\alpha", r"|0\rangle",
            "+", r"\beta", r"|1\rangle",
            font_size=52,
        )
        superposition_eq[0].set_color(QWHITE)
        superposition_eq[2].set_color(QBLUE)
        superposition_eq[3].set_color(QBLUE)
        superposition_eq[5].set_color(QRED)
        superposition_eq[6].set_color(QRED)

        self.play(Write(superposition_eq), run_time=2)
        self.wait(LONG_PAUSE)

        # Beat 5 - Normalization constraint
        norm_eq = MathTex(
            r"|\alpha|^2 + |\beta|^2 = 1",
            font_size=40, color=QGREEN,
        ).next_to(superposition_eq, UP, buff=1.0)
        norm_box = SurroundingRectangle(norm_eq, color=QGREEN, corner_radius=0.1, buff=0.2)

        self.play(Write(norm_eq), Create(norm_box))
        self.play(Indicate(norm_eq, color=QGREEN, scale_factor=1.2))
        self.wait(LONG_PAUSE)
        self.clear_scene()
