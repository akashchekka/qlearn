"""2.2 - Circuit Notation

Teaching objective: teach how to read a quantum circuit step by step.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QWHITE, QGRAY, QGREEN, QCYAN, QPURPLE, QYELLOW,
    STEP_PAUSE, LONG_PAUSE,
)
from common.circuit import QuantumCircuit


class CircuitNotationScene(QScene):
    def construct(self):
        self.show_title_card("Circuit Notation")

        sec = self.show_section("Reading a Circuit", QCYAN)

        qc = QuantumCircuit(num_qubits=2, num_cols=5, wire_length=7.0, labels=["0", "0"])
        qc.move_to(LEFT * 0.5)
        self.play(FadeIn(qc), run_time=1.5)
        self.pause()

        # H gate on q0
        h_gate = qc.add_single_gate("H", 0, 1, color=QBLUE)
        self.play(FadeIn(h_gate), run_time=1.2)
        h_lbl = Text("Hadamard", font_size=22, color=QGRAY).next_to(h_gate, UP, buff=0.5)
        self.play(FadeIn(h_lbl, shift=UP * 0.2), run_time=0.6)
        self.pause()
        self.play(FadeOut(h_lbl))

        # CNOT
        cnot = qc.add_cnot(0, 1, 2, color=QCYAN)
        self.play(FadeIn(cnot), run_time=1.2)
        cnot_lbl = Text("CNOT", font_size=22, color=QGRAY).next_to(cnot, UP, buff=0.5)
        self.play(FadeIn(cnot_lbl, shift=UP * 0.2), run_time=0.6)
        self.pause()
        self.play(FadeOut(cnot_lbl))

        # Measurements
        m0 = qc.add_measurement(0, 4)
        m1 = qc.add_measurement(1, 4)
        self.play(FadeIn(m0), FadeIn(m1), run_time=1.2)
        self.pause()

        # Step-through highlight
        highlight = SurroundingRectangle(h_gate, color=QYELLOW, buff=0.1)
        self.play(Create(highlight), run_time=0.6)
        self.wait(0.5)
        self.play(highlight.animate.move_to(cnot), run_time=0.6)
        self.wait(0.5)
        self.play(highlight.animate.move_to(m0), run_time=0.6)
        self.wait(LONG_PAUSE)
        self.clear_scene()
