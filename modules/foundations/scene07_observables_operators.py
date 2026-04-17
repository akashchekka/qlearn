"""1.7 - Observables & Operators

Teaching objective: explain that physical quantities in QM are
represented by operators (matrices), and measurements yield eigenvalues.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QWHITE, QGRAY, QGREEN, QPURPLE, QORANGE,
    STEP_PAUSE, LONG_PAUSE, SMALL_MATH_SIZE,
)


class ObservablesOperatorsScene(QScene):
    def construct(self):
        self.show_title_card("Observables & Operators")

        # Beat 2 - What is an observable?
        sec = self.show_section("Observables", QPURPLE)
        obs_list = VGroup(
            Text("position,  momentum,  energy,  spin ...", font_size=28, color=QWHITE),
            Text("=  things you can measure", font_size=24, color=QGRAY),
        ).arrange(DOWN, buff=0.5).move_to(UP * 1.5)
        self.play(Write(obs_list[0]), run_time=1.5)
        self.play(Write(obs_list[1]), run_time=1.2)
        self.wait(LONG_PAUSE)
        self.fade_out_group(obs_list, sec)

        # Beat 3 - Operators as matrices
        sec2 = self.show_section("Operators = Matrices", QBLUE)
        op_eq = MathTex(
            r"\hat{A}", r"|\psi\rangle", r"= \text{transformed state}",
            font_size=32,
        )
        op_eq[0].set_color(QPURPLE)
        op_eq[1].set_color(QBLUE)
        op_eq[2].set_color(QGRAY)
        op_eq.move_to(UP * 1.5)
        self.play(Write(op_eq), run_time=2.0)

        hermitian = Text("observables use Hermitian operators  (real eigenvalues)",
                         font_size=24, color=QGRAY).next_to(op_eq, DOWN, buff=0.6)
        self.play(Write(hermitian))
        self.wait(LONG_PAUSE)
        self.fade_out_group(op_eq, hermitian, sec2)

        # Beat 4 - Eigenvalue equation
        sec3 = self.show_section("Eigenvalues", QGREEN)
        eigen = MathTex(
            r"\hat{A}", r"|a\rangle", r"=", r"a", r"|a\rangle",
            font_size=44,
        )
        eigen[0].set_color(QPURPLE)
        eigen[1].set_color(QBLUE)
        eigen[3].set_color(QGREEN)
        eigen[4].set_color(QBLUE)
        eigen.move_to(UP * 1.0)
        self.play(Write(eigen), run_time=2.0)

        eigen_labels = VGroup(
            VGroup(
                MathTex(r"|a\rangle", font_size=24, color=QBLUE),
                Text("=  eigenstate  (definite outcome)", font_size=22, color=QGRAY),
            ).arrange(RIGHT, buff=0.4),
            VGroup(
                MathTex(r"a", font_size=24, color=QGREEN),
                Text("=  eigenvalue  (measurement result)", font_size=22, color=QGRAY),
            ).arrange(RIGHT, buff=0.4),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(DOWN * 0.8)

        for lbl in eigen_labels:
            self.play(FadeIn(lbl, shift=LEFT * 0.3), run_time=1.2)
        self.wait(LONG_PAUSE)
        self.fade_out_group(eigen, eigen_labels, sec3)

        # Beat 5 - Example: spin-z
        sec4 = self.show_section("Example: Spin-Z", QORANGE)
        sz = MathTex(
            r"\hat{S}_z = \frac{\hbar}{2} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}",
            font_size=SMALL_MATH_SIZE, color=QORANGE,
        ).move_to(UP * 1.5)
        self.play(Write(sz), run_time=1.5)

        eigenvals = VGroup(
            MathTex(r"|{\uparrow}\rangle \to +\frac{\hbar}{2}", font_size=28, color=QBLUE),
            MathTex(r"|{\downarrow}\rangle \to -\frac{\hbar}{2}", font_size=28, color=QRED),
        ).arrange(DOWN, buff=0.4).move_to(DOWN * 0.5)
        self.play(Write(eigenvals[0]), Write(eigenvals[1]), run_time=1.8)

        meaning = Text("measurement always gives  one  of the eigenvalues",
                        font_size=24, color=QGREEN).to_edge(DOWN, buff=0.5)
        self.play(Write(meaning))
        self.wait(LONG_PAUSE)
        self.clear_scene()
