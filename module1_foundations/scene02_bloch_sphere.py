"""1.2 — The Bloch Sphere (animation only)"""
from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QPURPLE
from common.quantum import BlochSphere


class BlochSphereScene(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        bloch = BlochSphere(radius=1.8, theta=0, phi=0)
        bloch.move_to(LEFT * 2.5 + DOWN * 0.2)
        self.play(FadeIn(bloch, scale=0.8), run_time=1.5)

        # State label on the right
        state_lbl = MathTex(r"|\psi\rangle = |0\rangle", font_size=36, color=QBLUE)
        state_lbl.move_to(RIGHT * 3 + UP * 1.5)
        self.play(Write(state_lbl))
        self.wait(1)

        # |0⟩ → |1⟩
        lbl_1 = MathTex(r"|\psi\rangle = |1\rangle", font_size=36, color=QRED)
        lbl_1.move_to(state_lbl)
        self.play(bloch.animate_to_state(np.pi, 0), Transform(state_lbl, lbl_1), run_time=2)
        self.wait(1)

        # |1⟩ → |+⟩
        lbl_plus = MathTex(
            r"|\psi\rangle = |+\rangle = \tfrac{1}{\sqrt{2}}(|0\rangle + |1\rangle)",
            font_size=28, color=QGREEN,
        ).move_to(state_lbl)
        self.play(bloch.animate_to_state(np.pi / 2, 0), Transform(state_lbl, lbl_plus), run_time=2)
        self.wait(1)

        # |+⟩ → |−⟩
        lbl_minus = MathTex(
            r"|\psi\rangle = |-\rangle = \tfrac{1}{\sqrt{2}}(|0\rangle - |1\rangle)",
            font_size=28, color=QPURPLE,
        ).move_to(state_lbl)
        self.play(bloch.animate_to_state(np.pi / 2, np.pi), Transform(state_lbl, lbl_minus), run_time=2)
        self.wait(1)

        # Arbitrary state with θ, φ
        lbl_arb = MathTex(
            r"|\psi\rangle = \cos\tfrac{\theta}{2}|0\rangle + e^{i\phi}\sin\tfrac{\theta}{2}|1\rangle",
            font_size=26, color=QWHITE,
        ).move_to(state_lbl)
        self.play(bloch.animate_to_state(np.pi / 3, np.pi / 4), Transform(state_lbl, lbl_arb), run_time=2)
        self.wait(1)

        # Sweep around the sphere
        self.play(FadeOut(state_lbl))
        for angle in np.linspace(np.pi / 4, 2 * np.pi + np.pi / 4, 40):
            self.play(bloch.animate_to_state(np.pi / 3, angle), run_time=0.1, rate_func=linear)
        self.wait(1)
        self.play(FadeOut(bloch))
