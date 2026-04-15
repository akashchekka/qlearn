"""4.1 — Deutsch-Jozsa Algorithm (animation only)"""
from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QPURPLE, QORANGE
from common.circuit import QuantumCircuit


class DeutschJozsaScene(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        # ── Constant vs Balanced visual ──────────────────────
        const_box = VGroup(
            RoundedRectangle(width=3, height=1.6, corner_radius=0.15, color=QBLUE, fill_opacity=0.15),
            MathTex(r"f(x) = 0 \;\forall x", font_size=24, color=QWHITE),
        ).move_to(LEFT * 3)
        bal_box = VGroup(
            RoundedRectangle(width=3, height=1.6, corner_radius=0.15, color=QRED, fill_opacity=0.15),
            MathTex(r"\text{Half } 0, \text{ half } 1", font_size=24, color=QWHITE),
        ).move_to(RIGHT * 3)

        self.play(FadeIn(const_box, shift=UP * 0.2), FadeIn(bal_box, shift=UP * 0.2))
        self.wait(2)
        self.play(FadeOut(const_box), FadeOut(bal_box))

        # ── Circuit (2-qubit Deutsch) ─────────────────────────
        circ = QuantumCircuit(num_qubits=2, num_cols=7, wire_length=9, labels=["0", "1"])
        self.play(FadeIn(circ))

        h0 = circ.add_single_gate("H", 0, 1, color=QGREEN)
        h1 = circ.add_single_gate("H", 1, 1, color=QGREEN)
        self.play(FadeIn(h0, scale=1.2), FadeIn(h1, scale=1.2))

        # Oracle box spanning both qubits
        op0 = circ.gate_position(0, 3)
        op1 = circ.gate_position(1, 3)
        oracle_box = Rectangle(width=0.9, height=op0[1] - op1[1] + 0.8,
                               color=QORANGE, fill_opacity=0.2, stroke_width=2)
        oracle_box.move_to((op0 + op1) / 2)
        oracle_lbl = MathTex(r"U_f", font_size=24, color=QORANGE).move_to(oracle_box)
        oracle = VGroup(oracle_box, oracle_lbl)
        self.play(FadeIn(oracle, scale=1.2))

        h_final = circ.add_single_gate("H", 0, 5, color=QBLUE)
        self.play(FadeIn(h_final, scale=1.2))

        m0 = circ.add_measurement(0, 6, color=QGREEN)
        self.play(FadeIn(m0, scale=1.2))
        self.wait(1)

        # Result
        results = VGroup(
            MathTex(r"|0\rangle \Rightarrow \text{constant}", font_size=28, color=QBLUE),
            MathTex(r"|1\rangle \Rightarrow \text{balanced}", font_size=28, color=QRED),
        ).arrange(DOWN, buff=0.3).to_edge(DOWN, buff=0.4)
        self.play(Write(results), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(circ), FadeOut(h0), FadeOut(h1), FadeOut(oracle),
                  FadeOut(h_final), FadeOut(m0), FadeOut(results))

        # ── Speedup comparison ────────────────────────────────
        speedup = VGroup(
            MathTex(r"\text{Classical: } O(2^{n-1}+1)", font_size=32, color=QRED),
            MathTex(r"\text{Quantum: } O(1)", font_size=32, color=QGREEN),
        ).arrange(RIGHT, buff=2.0)
        self.play(Write(speedup))
        self.wait(2)
        self.play(FadeOut(speedup))
