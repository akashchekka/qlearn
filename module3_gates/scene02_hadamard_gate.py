"""2.2 — The Hadamard Gate (animation only)"""
from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QORANGE
from common.quantum import BlochSphere
from common.circuit import QuantumCircuit


class HadamardGateScene(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        # ── Matrix ────────────────────────────────────────────
        h_matrix = MathTex(
            r"H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}",
            font_size=40, color=QGREEN,
        )
        self.play(Write(h_matrix), run_time=1.5)
        self.wait(1)

        # ── Effects ───────────────────────────────────────────
        self.play(h_matrix.animate.scale(0.7).to_edge(UP, buff=0.5))

        eff_0 = MathTex(r"H|0\rangle = \tfrac{1}{\sqrt{2}}(|0\rangle + |1\rangle) = |+\rangle",
                        font_size=34, color=QBLUE).move_to(UP * 0.5)
        eff_1 = MathTex(r"H|1\rangle = \tfrac{1}{\sqrt{2}}(|0\rangle - |1\rangle) = |-\rangle",
                        font_size=34, color=QRED).move_to(DOWN * 0.5)
        self.play(Write(eff_0))
        self.play(Write(eff_1))
        self.wait(1.5)
        self.play(FadeOut(eff_0), FadeOut(eff_1), FadeOut(h_matrix))

        # ── Bloch sphere: |0⟩ → |+⟩ → |0⟩ ───────────────────
        bloch = BlochSphere(radius=1.5, theta=0, phi=0)
        bloch.move_to(ORIGIN)
        state_lbl = MathTex(r"|0\rangle", font_size=36, color=QBLUE).to_corner(UR, buff=0.6)
        self.play(FadeIn(bloch, scale=0.8), Write(state_lbl))
        self.wait(0.5)

        # H: |0⟩ → |+⟩
        lbl_plus = MathTex(r"H \to |+\rangle", font_size=36, color=QGREEN).to_corner(UR, buff=0.6)
        self.play(bloch.animate_to_state(np.pi / 2, 0), Transform(state_lbl, lbl_plus), run_time=2)
        self.wait(1)

        # H again: |+⟩ → |0⟩
        lbl_back = MathTex(r"H \to |0\rangle", font_size=36, color=QBLUE).to_corner(UR, buff=0.6)
        self.play(bloch.animate_to_state(0, 0), Transform(state_lbl, lbl_back), run_time=2)
        self.wait(0.5)

        hh_eq = MathTex(r"H \cdot H = I", font_size=40, color=QORANGE).to_edge(DOWN, buff=0.5)
        self.play(Write(hh_eq))
        self.wait(1.5)
        self.play(FadeOut(bloch), FadeOut(state_lbl), FadeOut(hh_eq))

        # ── Circuit: H gate + measurement ─────────────────────
        circ = QuantumCircuit(num_qubits=1, num_cols=4, wire_length=6, labels=["0"])
        self.play(FadeIn(circ))
        h_gate = circ.add_single_gate("H", 0, 1, color=QGREEN)
        self.play(FadeIn(h_gate, scale=1.2))
        meas = circ.add_measurement(0, 3, color=QORANGE)
        self.play(FadeIn(meas, scale=1.2))
        self.wait(2)
        self.play(FadeOut(circ), FadeOut(h_gate), FadeOut(meas))
