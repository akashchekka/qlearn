"""3.2 - Hadamard Gate

Teaching objective: H matrix, action, self-inverse, circuit role.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QWHITE, QGRAY, QGREEN, QORANGE, QPURPLE,
    STEP_PAUSE, LONG_PAUSE, SMALL_MATH_SIZE,
)
from common.quantum import BlochSphere

EQ_X = 3.2
SPHERE_POS = LEFT * 2.5 + DOWN * 0.3


class HadamardGateScene(QScene):
    def construct(self):
        self.show_title_card("Hadamard Gate")

        # Beat 2 - Matrix
        sec = self.show_section("H Matrix", QGREEN)
        mat = MathTex(
            r"H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}",
            font_size=SMALL_MATH_SIZE, color=QGREEN,
        ).move_to(UP * 1.5)
        self.play(Write(mat), run_time=1.5)
        self.pause()

        # Beat 3 - Action
        action1 = MathTex(r"H|0\rangle = |+\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}",
                          font_size=SMALL_MATH_SIZE, color=QWHITE).move_to(DOWN * 0.5)
        action2 = MathTex(r"H|1\rangle = |-\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}",
                          font_size=SMALL_MATH_SIZE, color=QWHITE).next_to(action1, DOWN, buff=0.6)
        self.play(Write(action1), run_time=1.5)
        self.play(Write(action2), run_time=1.5)
        self.wait(LONG_PAUSE)
        self.fade_out_group(mat, action1, action2, sec)

        # Beat 4 - Bloch view
        sec2 = self.show_section("Bloch View", QGREEN)
        bloch = BlochSphere(radius=1.4, theta=0, phi=0)
        bloch.move_to(SPHERE_POS)
        eq_lbl = MathTex(r"|0\rangle \to |+\rangle", font_size=SMALL_MATH_SIZE,
                         color=QGREEN).move_to(RIGHT * EQ_X + UP * 1.5)
        self.play(FadeIn(bloch, scale=0.8), Write(eq_lbl))
        self.play(bloch.animate_to_state(np.pi / 2, 0), run_time=1.5)
        self.wait(LONG_PAUSE)

        # Beat 5 - Self-inverse
        eq_inv = MathTex(r"H^2 = I", font_size=32, color=QORANGE
                         ).move_to(RIGHT * EQ_X + DOWN * 0.5)
        self.play(Write(eq_inv))
        self.play(Indicate(eq_inv), run_time=0.8)
        self.play(Circumscribe(eq_inv, color=QORANGE), run_time=0.8)
        self.play(bloch.animate_to_state(0, 0), run_time=1.5)
        self.wait(LONG_PAUSE)
        self.clear_scene()
