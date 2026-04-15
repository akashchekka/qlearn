"""2.4 — Multi-Qubit Gates (animation only)"""
from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QPURPLE, QORANGE
from common.circuit import QuantumCircuit


class MultiQubitGatesScene(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        # ── CNOT ──────────────────────────────────────────────
        circ = QuantumCircuit(num_qubits=2, num_cols=5, wire_length=7, labels=["ctrl", "tgt"])
        circ.move_to(UP * 1.0)
        self.play(FadeIn(circ))
        cnot = circ.add_cnot(0, 1, 2, color=QBLUE)
        self.play(FadeIn(cnot, scale=1.2))

        truth = VGroup(
            MathTex(r"|00\rangle \to |00\rangle", font_size=24, color=QWHITE),
            MathTex(r"|01\rangle \to |01\rangle", font_size=24, color=QWHITE),
            MathTex(r"|10\rangle \to |11\rangle", font_size=24, color=QORANGE),
            MathTex(r"|11\rangle \to |10\rangle", font_size=24, color=QORANGE),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).move_to(DOWN * 1.5)
        self.play(Write(truth), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(circ), FadeOut(cnot), FadeOut(truth))

        # ── SWAP ──────────────────────────────────────────────
        circ2 = QuantumCircuit(num_qubits=2, num_cols=5, wire_length=7, labels=["a", "b"])
        circ2.move_to(UP * 0.5)
        self.play(FadeIn(circ2))
        swap = circ2.add_swap(0, 1, 2, color=QGREEN)
        self.play(FadeIn(swap, scale=1.2))

        swap_eq = MathTex(r"\text{SWAP}|a,b\rangle = |b,a\rangle", font_size=32, color=QWHITE).move_to(DOWN * 1.2)
        self.play(Write(swap_eq))
        self.wait(2)
        self.play(FadeOut(circ2), FadeOut(swap), FadeOut(swap_eq))

        # ── Toffoli ───────────────────────────────────────────
        circ3 = QuantumCircuit(num_qubits=3, num_cols=5, wire_length=7, labels=["c_1", "c_2", "tgt"])
        self.play(FadeIn(circ3))

        c1 = circ3.gate_position(0, 2)
        c2 = circ3.gate_position(1, 2)
        tgt = circ3.gate_position(2, 2)
        toffoli = VGroup(
            Line(c1, tgt, color=QPURPLE, stroke_width=2),
            Dot(c1, color=QPURPLE, radius=0.1),
            Dot(c2, color=QPURPLE, radius=0.1),
            Circle(radius=0.2, color=QPURPLE, stroke_width=2).move_to(tgt),
            MathTex(r"+", font_size=18, color=QPURPLE).move_to(tgt),
        )
        self.play(FadeIn(toffoli, scale=1.2))
        self.wait(2)
        self.play(FadeOut(circ3), FadeOut(toffoli))
