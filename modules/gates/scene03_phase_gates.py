"""3.3 - Phase & Rotation Gates

Teaching objective: Z, S, T hierarchy and generalized rotations.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QWHITE, QGRAY, QPURPLE, QORANGE, QYELLOW,
    STEP_PAUSE, LONG_PAUSE, SMALL_MATH_SIZE,
)
from common.quantum import BlochSphere

EQ_X = 3.2
SPHERE_POS = LEFT * 2.5 + DOWN * 0.3


class PhaseGatesScene(QScene):
    def construct(self):
        self.show_title_card("Phase & Rotation Gates")

        phase_gates = [
            ("Z", r"\begin{pmatrix}1&0\\0&-1\end{pmatrix}", r"\pi", np.pi),
            ("S", r"\begin{pmatrix}1&0\\0&i\end{pmatrix}", r"\pi/2", np.pi/2),
            ("T", r"\begin{pmatrix}1&0\\0&e^{i\pi/4}\end{pmatrix}", r"\pi/4", np.pi/4),
        ]

        for name, mat_str, angle_str, angle in phase_gates:
            sec = self.show_section(f"{name} Gate", QPURPLE)
            mat = MathTex(mat_str, font_size=SMALL_MATH_SIZE, color=QPURPLE
                          ).move_to(LEFT * 4 + UP * 1.5)
            rot_lbl = MathTex(f"R_z({angle_str})", font_size=SMALL_MATH_SIZE, color=QYELLOW
                              ).move_to(RIGHT * EQ_X + UP * 1.5)

            bloch = BlochSphere(radius=1.2, theta=np.pi/2, phi=0)
            bloch.move_to(SPHERE_POS)

            self.play(Write(mat), Write(rot_lbl), run_time=1.5)
            self.play(FadeIn(bloch, scale=0.8), run_time=1.2)
            self.play(bloch.animate_to_state(np.pi/2, angle), run_time=1.5)
            self.wait(LONG_PAUSE)
            self.fade_out_group(mat, rot_lbl, bloch, sec)

        # Hierarchy
        sec_h = self.show_section("Hierarchy", QORANGE)
        hier = MathTex(r"Z = S^2 = T^4", font_size=36, color=QORANGE).move_to(ORIGIN)
        self.play(Write(hier), run_time=1.5)
        self.play(Indicate(hier), run_time=0.8)
        self.play(Circumscribe(hier, color=QORANGE), run_time=0.8)
        self.wait(LONG_PAUSE)
        self.clear_scene()
