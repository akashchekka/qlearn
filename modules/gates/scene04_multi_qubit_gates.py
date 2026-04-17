"""3.4 - Multi-Qubit Gates

Teaching objective: CNOT, SWAP, Toffoli gates.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QWHITE, QGRAY, QGREEN, QCYAN, QPURPLE, QORANGE,
    STEP_PAUSE, LONG_PAUSE, SMALL_MATH_SIZE,
)
from common.circuit import QuantumCircuit


class MultiQubitGatesScene(QScene):
    def construct(self):
        self.show_title_card("Multi-Qubit Gates")

        # Beat 2 - CNOT
        sec = self.show_section("CNOT Gate", QCYAN)
        qc = QuantumCircuit(num_qubits=2, num_cols=3, wire_length=5.0, labels=["0", "0"])
        qc.move_to(LEFT * 2.5 + UP * 0.5)
        self.play(FadeIn(qc))
        cnot = qc.add_cnot(0, 1, 1, color=QCYAN)
        self.play(FadeIn(cnot), run_time=1.2)

        truth = MathTex(
            r"|00\rangle \to |00\rangle \quad |01\rangle \to |01\rangle",
            r"\quad |10\rangle \to |11\rangle \quad |11\rangle \to |10\rangle",
            font_size=26, color=QWHITE,
        ).move_to(RIGHT * 2.5 + UP * 0.5)
        self.play(Write(truth), run_time=1.2)
        self.wait(LONG_PAUSE)
        self.fade_out_group(qc, cnot, truth, sec)

        # Beat 3 - SWAP
        sec2 = self.show_section("SWAP Gate", QORANGE)
        qc2 = QuantumCircuit(num_qubits=2, num_cols=3, wire_length=5.0, labels=["a", "b"])
        qc2.move_to(LEFT * 2.5 + UP * 0.5)
        self.play(FadeIn(qc2))
        swap = qc2.add_swap(0, 1, 1, color=QORANGE)
        self.play(FadeIn(swap), run_time=1.2)

        swap_eq = MathTex(r"|ab\rangle \to |ba\rangle", font_size=28, color=QWHITE
                          ).move_to(RIGHT * 2.5 + UP * 0.5)
        self.play(Write(swap_eq), run_time=1.5)
        self.wait(LONG_PAUSE)
        self.fade_out_group(qc2, swap, swap_eq, sec2)

        # Beat 4 - Toffoli
        sec3 = self.show_section("Toffoli (CCX)", QPURPLE)
        qc3 = QuantumCircuit(num_qubits=3, num_cols=3, wire_length=5.0, labels=["0", "0", "0"])
        qc3.move_to(LEFT * 2.5 + UP * 0.5)
        self.play(FadeIn(qc3))
        # Two controls + target
        tgt_pos = qc3.gate_position(2, 1)
        ctrl1_pos = qc3.gate_position(0, 1)
        ctrl2_pos = qc3.gate_position(1, 1)
        c1 = Dot(ctrl1_pos, color=QPURPLE, radius=0.1)
        c2 = Dot(ctrl2_pos, color=QPURPLE, radius=0.1)
        tgt_c = Circle(radius=0.2, color=QPURPLE, stroke_width=2).move_to(tgt_pos)
        tgt_p = MathTex("+", font_size=22, color=QPURPLE).move_to(tgt_pos)
        line = Line(ctrl1_pos, tgt_pos, color=QPURPLE, stroke_width=2)
        toffoli = VGroup(line, c1, c2, tgt_c, tgt_p)
        qc3.add(toffoli)
        self.play(FadeIn(toffoli), run_time=1.2)

        toff_note = Text("universal  for  classical  reversible  logic", font_size=22,
                         color=QGRAY).move_to(RIGHT * 2.5 + UP * 0.5)
        self.play(Write(toff_note), run_time=1.5)
        self.wait(LONG_PAUSE)
        self.clear_scene()
