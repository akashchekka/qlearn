"""4.2 - Quantum Teleportation

Teaching objective: walk through the teleportation protocol.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QWHITE, QGRAY, QGREEN, QORANGE, QYELLOW,
    STEP_PAUSE, LONG_PAUSE, SMALL_MATH_SIZE,
)
from common.circuit import QuantumCircuit


class QuantumTeleportationScene(QScene):
    def construct(self):
        self.show_title_card("Quantum Teleportation")

        # Beat 2 - Alice and Bob
        sec = self.show_section("Setup", QBLUE)
        alice = Text("Alice", font_size=28, color=QBLUE).move_to(LEFT * 4.5 + UP * 2.5)
        bob = Text("Bob", font_size=28, color=QRED).move_to(RIGHT * 4.5 + UP * 2.5)
        self.play(Write(alice), Write(bob))

        # Beat 3 - Circuit
        qc = QuantumCircuit(num_qubits=3, num_cols=6, wire_length=8.0,
                            labels=["\\psi", "0", "0"])
        qc.move_to(DOWN * 0.3)
        self.play(FadeIn(qc), run_time=1.5)

        cnot1 = qc.add_cnot(1, 2, 1, color=QORANGE)
        h1 = qc.add_single_gate("H", 1, 0, color=QBLUE)
        self.play(FadeIn(h1), FadeIn(cnot1), run_time=1.2)
        self.pause()

        # Beat 4 - Bell measurement on psi and Alice-half
        cnot2 = qc.add_cnot(0, 1, 3, color=QBLUE)
        h2 = qc.add_single_gate("H", 0, 4, color=QBLUE)
        self.play(FadeIn(cnot2), FadeIn(h2), run_time=1.2)
        m0 = qc.add_measurement(0, 5)
        m1 = qc.add_measurement(1, 5)
        self.play(FadeIn(m0), FadeIn(m1), run_time=1.2)
        self.pause()

        # Beat 5 - Classical bits to Bob
        classical_note = Text("2  classical  bits  to  Bob", font_size=22, color=QGRAY
                              ).move_to(DOWN * 2.8)
        self.play(FadeIn(classical_note, shift=UP * 0.3))
        self.wait(LONG_PAUSE)

        # Beat 6 - Result
        result_note = MathTex(r"\text{Bob has } |\psi\rangle", font_size=28, color=QGREEN
                              ).move_to(DOWN * 3.5)
        noclone = Text("original  destroyed  (no-cloning)", font_size=20, color=QGRAY
                       ).next_to(result_note, DOWN, buff=0.25)
        self.play(Write(result_note), Write(noclone))
        self.play(Indicate(result_note, color=QORANGE))
        self.wait(LONG_PAUSE)
        self.clear_scene()
