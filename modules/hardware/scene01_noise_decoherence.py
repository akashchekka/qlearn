"""6.1 - Noise & Decoherence

Teaching objective: T1, T2, noise models, fidelity.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QWHITE, QGRAY, QGREEN, QORANGE, QPURPLE, QYELLOW,
    STEP_PAUSE, LONG_PAUSE, SMALL_MATH_SIZE,
)
from common.quantum import BlochSphere

EQ_X = 3.5
SPHERE_POS = LEFT * 2.5 + DOWN * 0.3


class NoiseDecoherenceScene(QScene):
    def construct(self):
        self.show_title_card("Noise & Decoherence")

        # Beat 2 - T2 dephasing
        sec = self.show_section("T2 Dephasing", QPURPLE)
        bloch = BlochSphere(radius=1.3, theta=np.pi/2, phi=0)
        bloch.move_to(SPHERE_POS)
        t2_lbl = MathTex(r"T_2: \text{phase lost}", font_size=SMALL_MATH_SIZE, color=QPURPLE
                         ).move_to(RIGHT * EQ_X + UP * 1.5)
        self.play(FadeIn(bloch, scale=0.8), Write(t2_lbl))
        # Spiral toward z-axis (simplify: move to north)
        self.play(bloch.animate_to_state(0.1, 0), run_time=2.5)
        self.wait(LONG_PAUSE)
        self.fade_out_group(bloch, t2_lbl, sec)

        # Beat 3 - T1 relaxation
        sec2 = self.show_section("T1 Relaxation", QORANGE)
        bloch2 = BlochSphere(radius=1.3, theta=np.pi, phi=0)
        bloch2.move_to(SPHERE_POS)
        t1_lbl = MathTex(r"T_1: \text{energy lost}", font_size=SMALL_MATH_SIZE, color=QORANGE
                         ).move_to(RIGHT * EQ_X + UP * 1.5)
        self.play(FadeIn(bloch2, scale=0.8), Write(t1_lbl))
        self.play(bloch2.animate_to_state(0, 0), run_time=2.5)
        self.wait(LONG_PAUSE)
        self.fade_out_group(bloch2, t1_lbl, sec2)

        # Beat 5 - Noise models
        sec3 = self.show_section("Noise Models", QGRAY)
        models = VGroup(
            VGroup(
                Rectangle(width=3.0, height=0.8, color=QRED, fill_opacity=0.1),
                Text("bit-flip:  X  with  prob  p", font_size=22, color=QWHITE),
            ),
            VGroup(
                Rectangle(width=3.0, height=0.8, color=QPURPLE, fill_opacity=0.1),
                Text("phase-flip:  Z  with  prob  p", font_size=22, color=QWHITE),
            ),
            VGroup(
                Rectangle(width=3.0, height=0.8, color=QORANGE, fill_opacity=0.1),
                Text("depolarizing:  random  Pauli", font_size=22, color=QWHITE),
            ),
        ).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        self.play(FadeIn(models), run_time=1.5)
        self.wait(LONG_PAUSE)

        # Beat 6 - Fidelity
        self.clear_scene()
        sec4 = self.show_section("Fidelity", QGREEN)
        fid = MathTex(r"F = \langle\psi|\rho|\psi\rangle", font_size=36, color=QGREEN
                      ).move_to(UP * 0.5)
        fid_note = Text("how  close  is  the  noisy  state  to  ideal", font_size=24, color=QGRAY
                        ).next_to(fid, DOWN, buff=0.5)
        self.play(Write(fid), FadeIn(fid_note, shift=UP * 0.3))
        self.play(Indicate(fid))
        self.wait(LONG_PAUSE)
        self.clear_scene()
