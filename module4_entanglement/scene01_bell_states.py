"""3.1 — Bell States & Entanglement (animation only)"""
from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QPURPLE, QORANGE
from common.circuit import QuantumCircuit


class BellStatesScene(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        # ── Step-by-step state evolution ──────────────────────
        step1 = MathTex(r"|00\rangle", font_size=40, color=QWHITE).move_to(UP * 1.5)
        self.play(Write(step1))
        self.wait(0.8)

        step2 = MathTex(
            r"\xrightarrow{H \otimes I}",
            r"\tfrac{1}{\sqrt{2}}(|0\rangle + |1\rangle)|0\rangle",
            font_size=32, color=QGREEN,
        ).move_to(UP * 0.2)
        self.play(Write(step2))
        self.wait(1)

        step3 = MathTex(
            r"\xrightarrow{\text{CNOT}}",
            r"\tfrac{1}{\sqrt{2}}(|00\rangle + |11\rangle)",
            font_size=32, color=QPURPLE,
        ).move_to(DOWN * 1.0)
        self.play(Write(step3))

        bell_box = SurroundingRectangle(step3[1], color=QPURPLE, corner_radius=0.1, buff=0.15)
        bell_lbl = MathTex(r"|\Phi^+\rangle", font_size=36, color=QPURPLE).next_to(bell_box, DOWN, buff=0.3)
        self.play(Create(bell_box), Write(bell_lbl))
        self.wait(2)
        self.play(FadeOut(step1), FadeOut(step2), FadeOut(step3), FadeOut(bell_box), FadeOut(bell_lbl))

        # ── Circuit ───────────────────────────────────────────
        circ = QuantumCircuit(num_qubits=2, num_cols=6, wire_length=8, labels=["0", "0"])
        circ.move_to(UP * 0.5)
        self.play(FadeIn(circ))
        h_gate = circ.add_single_gate("H", 0, 1, color=QGREEN)
        self.play(FadeIn(h_gate, scale=1.2))
        cnot = circ.add_cnot(0, 1, 3, color=QPURPLE)
        self.play(FadeIn(cnot, scale=1.2))

        output = MathTex(r"\tfrac{1}{\sqrt{2}}(|00\rangle + |11\rangle)", font_size=30, color=QPURPLE)
        output.next_to(circ, DOWN, buff=0.8)
        self.play(Write(output))
        self.wait(2)
        self.play(FadeOut(circ), FadeOut(h_gate), FadeOut(cnot), FadeOut(output))

        # ── Four Bell States ──────────────────────────────────
        bells = VGroup(
            MathTex(r"|\Phi^+\rangle = \tfrac{1}{\sqrt{2}}(|00\rangle + |11\rangle)", font_size=30, color=QBLUE),
            MathTex(r"|\Phi^-\rangle = \tfrac{1}{\sqrt{2}}(|00\rangle - |11\rangle)", font_size=30, color=QRED),
            MathTex(r"|\Psi^+\rangle = \tfrac{1}{\sqrt{2}}(|01\rangle + |10\rangle)", font_size=30, color=QGREEN),
            MathTex(r"|\Psi^-\rangle = \tfrac{1}{\sqrt{2}}(|01\rangle - |10\rangle)", font_size=30, color=QPURPLE),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        for bs in bells:
            self.play(Write(bs), run_time=0.8)
            self.wait(0.3)
        self.wait(1.5)
        self.play(FadeOut(bells))

        # ── Spooky action correlation ─────────────────────────
        qubit_a = VGroup(
            Circle(radius=0.5, color=QBLUE, fill_opacity=0.3),
            MathTex(r"A", font_size=22, color=QBLUE).shift(0.9 * DOWN),
        ).move_to(LEFT * 4)
        qubit_b = VGroup(
            Circle(radius=0.5, color=QRED, fill_opacity=0.3),
            MathTex(r"B", font_size=22, color=QRED).shift(0.9 * DOWN),
        ).move_to(RIGHT * 4)
        ent_line = DashedLine(qubit_a[0].get_right(), qubit_b[0].get_left(), color=QPURPLE, stroke_opacity=0.5)

        self.play(FadeIn(qubit_a), FadeIn(qubit_b), Create(ent_line))
        self.wait(0.5)

        # Alice measures → |0⟩
        flash_a = Circle(radius=0.01, color=QGREEN, fill_opacity=1).move_to(qubit_a[0])
        self.play(flash_a.animate.scale(50).set_opacity(0), run_time=0.4)
        res_a = MathTex(r"|0\rangle", font_size=36, color=QBLUE).next_to(qubit_a, UP, buff=0.5)
        self.play(Write(res_a))

        # Bob instantly |0⟩
        flash_b = Circle(radius=0.01, color=QGREEN, fill_opacity=1).move_to(qubit_b[0])
        self.play(flash_b.animate.scale(50).set_opacity(0), run_time=0.4)
        res_b = MathTex(r"|0\rangle", font_size=36, color=QRED).next_to(qubit_b, UP, buff=0.5)
        self.play(Write(res_b))
        self.wait(2)
        self.play(FadeOut(qubit_a), FadeOut(qubit_b), FadeOut(ent_line), FadeOut(res_a), FadeOut(res_b))
