"""2.2 — Circuit Notation & Reading Diagrams (animation only)"""
from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QPURPLE, QCYAN, QORANGE, QYELLOW
from common.circuit import QuantumCircuit, GATE_SIZE


class CircuitNotationScene(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        # ── Part 1: Wire labelling conventions ────────────────
        sec1 = Text("Wire Labels", font_size=32, color=QCYAN, weight=BOLD)
        sec1.to_edge(UP, buff=0.5)
        self.play(Write(sec1))

        # Show three wires with different label styles
        qc = QuantumCircuit(num_qubits=3, num_cols=6, wire_length=6.0,
                            labels=[r"\psi", "0", "1"])
        qc.shift(DOWN * 0.2)
        self.play(FadeIn(qc))
        self.wait(0.5)

        annot = VGroup(
            Text("Arbitrary state", font_size=16, color=QYELLOW),
            Text("Initialized to |0⟩", font_size=16, color=QBLUE),
            Text("Initialized to |1⟩", font_size=16, color=QRED),
        )
        for i, a in enumerate(annot):
            a.next_to(qc.wires[i], RIGHT, buff=0.5)
        self.play(*[Write(a) for a in annot])
        self.wait(1.5)
        self.play(FadeOut(qc), FadeOut(annot), FadeOut(sec1))

        # ── Part 2: Gate notation zoology ─────────────────────
        sec2 = Text("Gate Notation", font_size=32, color=QCYAN, weight=BOLD)
        sec2.to_edge(UP, buff=0.5)
        self.play(Write(sec2))

        qc2 = QuantumCircuit(num_qubits=3, num_cols=8, wire_length=9.0,
                             labels=["q_0", "q_1", "q_2"])
        qc2.shift(DOWN * 0.2)
        self.play(FadeIn(qc2))
        self.wait(0.3)

        # Single-qubit gate
        g1 = qc2.add_single_gate("X", 0, 1, color=QRED)
        lbl1 = Text("Single-qubit\ngate", font_size=14, color=QRED).next_to(g1, UP, buff=0.4)
        self.play(FadeIn(g1, scale=0.5), Write(lbl1))
        self.wait(0.5)

        # Controlled gate
        g2 = qc2.add_cnot(0, 1, 3, color=QPURPLE)
        lbl2 = Text("CNOT\n(controlled)", font_size=14, color=QPURPLE).next_to(g2, UP, buff=0.4)
        self.play(FadeIn(g2, scale=0.5), Write(lbl2))
        self.wait(0.5)

        # Controlled-U gate
        g3 = qc2.add_controlled_gate("U", 1, 2, 5, color=QORANGE)
        lbl3 = Text("Controlled-U", font_size=14, color=QORANGE).next_to(g3, DOWN, buff=0.4)
        self.play(FadeIn(g3, scale=0.5), Write(lbl3))
        self.wait(0.5)

        # Measurement
        g4 = qc2.add_measurement(2, 7, color=QGREEN)
        lbl4 = Text("Measurement", font_size=14, color=QGREEN).next_to(g4, DOWN, buff=0.4)
        self.play(FadeIn(g4, scale=0.5), Write(lbl4))
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in [qc2, lbl1, lbl2, lbl3, lbl4, sec2]])

        # ── Part 3: Reading a circuit step by step ────────────
        sec3 = Text("Reading a Circuit", font_size=32, color=QCYAN, weight=BOLD)
        sec3.to_edge(UP, buff=0.5)
        self.play(Write(sec3))

        # Bell state circuit — read it column by column
        qc3 = QuantumCircuit(num_qubits=2, num_cols=5, wire_length=7.0,
                             labels=["0", "0"])
        qc3.shift(DOWN * 0.3)
        self.play(FadeIn(qc3))

        # Column highlight sweep
        state_labels = [
            MathTex(r"|00\rangle", font_size=30, color=QWHITE),
            MathTex(r"\tfrac{|0\rangle+|1\rangle}{\sqrt{2}}\;|0\rangle", font_size=26, color=QBLUE),
            MathTex(r"\tfrac{|00\rangle+|11\rangle}{\sqrt{2}}", font_size=28, color=QPURPLE),
        ]
        state_pos = DOWN * 2.3

        # Step 0: initial state
        state_labels[0].move_to(state_pos)
        step0 = Text("Step 0: Initial state", font_size=18, color=QGRAY).next_to(state_labels[0], DOWN, buff=0.2)
        self.play(Write(state_labels[0]), Write(step0))
        self.wait(1)

        # Step 1: H gate
        h = qc3.add_single_gate("H", 0, 1, color=QBLUE)
        col_box1 = SurroundingRectangle(h, color=QYELLOW, buff=0.15,
                                         stroke_width=2, stroke_opacity=0.7)
        state_labels[1].move_to(state_pos)
        step1 = Text("Step 1: Hadamard on q₀", font_size=18, color=QGRAY).next_to(state_labels[1], DOWN, buff=0.2)
        self.play(FadeIn(h, scale=0.5), Create(col_box1))
        self.play(Transform(state_labels[0], state_labels[1]), Transform(step0, step1))
        self.wait(1)

        # Step 2: CNOT
        cnot = qc3.add_cnot(0, 1, 2, color=QPURPLE)
        col_box2 = SurroundingRectangle(cnot, color=QYELLOW, buff=0.15,
                                         stroke_width=2, stroke_opacity=0.7)
        state_labels[2].move_to(state_pos)
        step2 = Text("Step 2: CNOT → entangled!", font_size=18, color=QGRAY).next_to(state_labels[2], DOWN, buff=0.2)
        self.play(FadeOut(col_box1), FadeIn(cnot, scale=0.5), Create(col_box2))
        self.play(Transform(state_labels[0], state_labels[2]), Transform(step0, step2))
        self.wait(1.5)

        # Step 3: Measurement
        m0 = qc3.add_measurement(0, 4, color=QGREEN)
        m1 = qc3.add_measurement(1, 4, color=QGREEN)
        col_box3 = SurroundingRectangle(VGroup(m0, m1), color=QYELLOW, buff=0.15,
                                         stroke_width=2, stroke_opacity=0.7)
        result = MathTex(r"|00\rangle \text{ or } |11\rangle", font_size=28, color=QGREEN).move_to(state_pos)
        step3 = Text("Step 3: Measure → collapse!", font_size=18, color=QGRAY).next_to(result, DOWN, buff=0.2)
        self.play(FadeOut(col_box2), FadeIn(m0, scale=0.5), FadeIn(m1, scale=0.5), Create(col_box3))
        self.play(Transform(state_labels[0], result), Transform(step0, step3))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])
