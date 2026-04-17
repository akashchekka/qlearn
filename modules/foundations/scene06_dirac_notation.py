"""1.6 - Dirac Notation

Teaching objective: introduce bra-ket notation as the language of
quantum mechanics. Keep it practical — kets, bras, inner products,
and how they connect to probabilities.
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


class DiracNotationScene(QScene):
    def construct(self):
        self.show_title_card("Dirac Notation")

        # Beat 2 - Kets
        sec = self.show_section("Kets", QBLUE)
        ket_eq = MathTex(
            r"|\psi\rangle", r" \quad\longleftrightarrow\quad",
            r"\text{quantum state (column vector)}",
            font_size=32,
        )
        ket_eq[0].set_color(QBLUE)
        ket_eq[2].set_color(QGRAY)
        ket_eq.move_to(UP * 1.5)
        self.play(Write(ket_eq), run_time=2.0)
        ket_example = MathTex(
            r"|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}",
            r"\qquad",
            r"|1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}",
            font_size=28,
        ).move_to(DOWN * 0.3)
        ket_example[0].set_color(QBLUE)
        ket_example[2].set_color(QRED)
        self.play(Write(ket_example), run_time=2.0)
        self.wait(LONG_PAUSE)
        self.fade_out_group(ket_eq, ket_example, sec)

        # Beat 3 - Bras
        sec2 = self.show_section("Bras", QRED)
        bra_eq = MathTex(
            r"\langle\psi|", r" \quad\longleftrightarrow\quad",
            r"\text{conjugate transpose (row vector)}",
            font_size=32,
        )
        bra_eq[0].set_color(QRED)
        bra_eq[2].set_color(QGRAY)
        bra_eq.move_to(UP * 1.5)
        self.play(Write(bra_eq), run_time=2.0)
        bra_example = MathTex(
            r"\langle 0| = \begin{pmatrix} 1 & 0 \end{pmatrix}",
            r"\qquad",
            r"\langle 1| = \begin{pmatrix} 0 & 1 \end{pmatrix}",
            font_size=28,
        ).move_to(DOWN * 0.3)
        bra_example[0].set_color(QBLUE)
        bra_example[2].set_color(QRED)
        self.play(Write(bra_example), run_time=2.0)
        self.wait(LONG_PAUSE)
        self.fade_out_group(bra_eq, bra_example, sec2)

        # Beat 4 - Inner product (braket)
        sec3 = self.show_section("Inner Product", QPURPLE)
        braket = MathTex(
            r"\langle\phi|\psi\rangle", r" = ", r"\text{overlap (complex number)}",
            font_size=32,
        )
        braket[0].set_color(QPURPLE)
        braket[2].set_color(QGRAY)
        braket.move_to(UP * 1.5)
        self.play(Write(braket), run_time=2.0)
        # Orthogonality
        ortho = VGroup(
            MathTex(r"\langle 0|0\rangle = 1", font_size=28, color=QGREEN),
            MathTex(r"\langle 1|1\rangle = 1", font_size=28, color=QGREEN),
            MathTex(r"\langle 0|1\rangle = 0", font_size=28, color=QORANGE),
        ).arrange(RIGHT, buff=1.0).move_to(DOWN * 0.3)
        self.play(Write(ortho[0]), Write(ortho[1]), run_time=1.5)
        self.play(Write(ortho[2]), run_time=1.2)
        self.play(Indicate(ortho[2], color=QORANGE, scale_factor=1.1))
        self.wait(LONG_PAUSE)
        self.fade_out_group(braket, ortho, sec3)

        # Beat 5 - Connection to probability
        sec4 = self.show_section("Probability", QGREEN)
        prob = MathTex(
            r"P(\text{outcome } |\phi\rangle) = |\langle\phi|\psi\rangle|^2",
            font_size=36, color=QWHITE,
        ).move_to(UP * 0.5)
        self.play(Write(prob), run_time=2.0)

        prob_note = Text("inner product squared  =  measurement probability",
                         font_size=24, color=QGREEN).next_to(prob, DOWN, buff=0.6)
        self.play(Write(prob_note))
        self.wait(LONG_PAUSE)
        self.clear_scene()
