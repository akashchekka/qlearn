"""3.1 - Pauli Gates

Teaching objective: introduce X, Y, Z gates via matrices, actions, and
Bloch-sphere rotations.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QWHITE, QGRAY, QPURPLE, QORANGE,
    STEP_PAUSE, LONG_PAUSE, SMALL_MATH_SIZE,
)
from common.quantum import BlochSphere

EQ_X = 3.2
SPHERE_POS = LEFT * 2.5 + DOWN * 0.3


class PauliGatesScene(QScene):
    def construct(self):
        self.show_title_card("Pauli Gates")

        gates = [
            ("X", r"\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}",
             r"X|0\rangle = |1\rangle", QRED, np.pi, 0),
            ("Y", r"\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}",
             r"Y|0\rangle = i|1\rangle", QPURPLE, np.pi, np.pi/2),
            ("Z", r"\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}",
             r"Z|1\rangle = -|1\rangle", QBLUE, np.pi, 0),
        ]

        for name, matrix_str, action_str, color, theta, phi in gates:
            sec = self.show_section(f"{name} Gate", color)

            mat = MathTex(matrix_str, font_size=SMALL_MATH_SIZE, color=color
                          ).move_to(LEFT * 4 + UP * 1.5)
            action = MathTex(action_str, font_size=SMALL_MATH_SIZE, color=QWHITE
                             ).move_to(RIGHT * EQ_X + UP * 1.5)

            bloch = BlochSphere(radius=1.2, theta=0, phi=0)
            bloch.move_to(SPHERE_POS)

            self.play(Write(mat), run_time=1.5)
            self.play(Write(action), run_time=1.5)
            self.play(Indicate(action), run_time=0.8)
            self.play(FadeIn(bloch, scale=0.8), run_time=1.2)
            self.play(bloch.animate_to_state(theta, phi), run_time=1.5)
            self.wait(LONG_PAUSE)
            self.fade_out_group(mat, action, bloch, sec)

        # Summary table
        sec_s = self.show_section("Summary", QGRAY)
        summary = VGroup(
            Text("X:  bit-flip,   Y:  bit+phase,   Z:  phase-flip", font_size=26, color=QWHITE),
        ).move_to(ORIGIN)
        self.play(Write(summary[0]))
        self.wait(LONG_PAUSE)
        self.clear_scene()
