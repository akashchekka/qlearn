"""5.3 - Quantum Fourier Transform

Teaching objective: QFT equation, roots of unity, 3-qubit circuit.
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
from common.circuit import QuantumCircuit


class QFTScene(QScene):
    def construct(self):
        self.show_title_card("Quantum Fourier Transform")

        # Beat 2 - QFT formula
        sec = self.show_section("QFT Formula", QPURPLE)
        formula = MathTex(
            r"|x\rangle \to \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} e^{2\pi i x k / N} |k\rangle",
            font_size=SMALL_MATH_SIZE, color=QWHITE,
        ).move_to(UP * 2.0)
        self.play(Write(formula), run_time=1.5)
        self.play(Indicate(formula))
        self.wait(LONG_PAUSE)
        self.play(FadeOut(formula), FadeOut(sec))

        # Beat 3 - Roots of unity
        sec2 = self.show_section("Roots of Unity", QPURPLE)
        circle = Circle(radius=1.5, color=QGRAY, stroke_opacity=0.4).move_to(LEFT * 2.5)
        self.play(Create(circle))

        N = 8
        dots = VGroup()
        for k in range(N):
            angle = 2 * np.pi * k / N
            pos = LEFT * 2.5 + 1.5 * np.array([np.cos(angle), np.sin(angle), 0])
            dot = Dot(pos, color=QPURPLE, radius=0.08)
            lbl = MathTex(str(k), font_size=20, color=QGRAY).next_to(dot, direction=
                          np.array([np.cos(angle), np.sin(angle), 0]), buff=0.15)
            dots.add(VGroup(dot, lbl))

        for d in dots:
            self.play(FadeIn(d), run_time=0.3)
        self.wait(LONG_PAUSE)
        self.fade_out_group(circle, dots, sec2)

        # Beat 4 - 3-qubit QFT circuit
        sec3 = self.show_section("3-Qubit Circuit", QPURPLE)
        qc = QuantumCircuit(num_qubits=3, num_cols=7, wire_length=8.0, labels=["0", "0", "0"])
        qc.move_to(ORIGIN)
        self.play(FadeIn(qc), run_time=1.5)

        h0 = qc.add_single_gate("H", 0, 1, color=QBLUE)
        r2 = qc.add_controlled_gate("R_2", 1, 0, 2, color=QPURPLE)
        r3 = qc.add_controlled_gate("R_3", 2, 0, 3, color=QPURPLE)
        h1 = qc.add_single_gate("H", 1, 4, color=QBLUE)
        r2b = qc.add_controlled_gate("R_2", 2, 1, 5, color=QPURPLE)
        h2 = qc.add_single_gate("H", 2, 6, color=QBLUE)

        for g in [h0, r2, r3, h1, r2b, h2]:
            self.play(FadeIn(g), run_time=0.5)
        self.wait(LONG_PAUSE)
        self.clear_scene()
