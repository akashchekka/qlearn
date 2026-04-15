"""2.1 — What Is a Quantum Circuit? (animation only)"""
from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QPURPLE, QCYAN, QORANGE
from common.circuit import QuantumCircuit


class WhatIsACircuitScene(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        # ── Classical circuit analogy ─────────────────────────
        title = Text("Classical Circuit", font_size=36, color=QWHITE, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        # Show classical logic gates as a simple diagram
        inp_a = Text("A", font_size=28, color=QBLUE).move_to(LEFT * 4 + UP * 0.5)
        inp_b = Text("B", font_size=28, color=QBLUE).move_to(LEFT * 4 + DOWN * 0.5)
        and_box = VGroup(
            RoundedRectangle(width=1.2, height=0.8, corner_radius=0.1, color=QGREEN,
                             fill_opacity=0.2, stroke_width=2),
            Text("AND", font_size=20, color=QGREEN),
        ).move_to(LEFT * 1.5)
        or_box = VGroup(
            RoundedRectangle(width=1.2, height=0.8, corner_radius=0.1, color=QORANGE,
                             fill_opacity=0.2, stroke_width=2),
            Text("OR", font_size=20, color=QORANGE),
        ).move_to(RIGHT * 1.5)
        out = Text("Out", font_size=28, color=QRED).move_to(RIGHT * 4)

        arrow1 = Arrow(inp_a.get_right(), and_box.get_left() + UP * 0.15, color=QGRAY, buff=0.15, stroke_width=2)
        arrow2 = Arrow(inp_b.get_right(), and_box.get_left() + DOWN * 0.15, color=QGRAY, buff=0.15, stroke_width=2)
        arrow3 = Arrow(and_box.get_right(), or_box.get_left(), color=QGRAY, buff=0.15, stroke_width=2)
        arrow4 = Arrow(or_box.get_right(), out.get_left(), color=QGRAY, buff=0.15, stroke_width=2)

        classical = VGroup(inp_a, inp_b, and_box, or_box, out, arrow1, arrow2, arrow3, arrow4)
        classical.shift(DOWN * 0.5)

        self.play(FadeIn(inp_a, shift=RIGHT * 0.3), FadeIn(inp_b, shift=RIGHT * 0.3))
        self.play(FadeIn(and_box, scale=0.8), GrowArrow(arrow1), GrowArrow(arrow2))
        self.play(FadeIn(or_box, scale=0.8), GrowArrow(arrow3))
        self.play(GrowArrow(arrow4), FadeIn(out, shift=LEFT * 0.3))
        self.wait(1)
        self.play(FadeOut(classical), FadeOut(title))

        # ── Transition to quantum circuit ─────────────────────
        q_title = Text("Quantum Circuit", font_size=36, color=QCYAN, weight=BOLD)
        q_title.to_edge(UP, buff=0.5)
        self.play(Write(q_title))

        # Build a simple 2-qubit circuit
        qc = QuantumCircuit(num_qubits=2, num_cols=5, wire_length=7.0,
                            labels=["0", "0"])
        qc.shift(DOWN * 0.3)
        self.play(FadeIn(qc, scale=0.9), run_time=1.5)
        self.wait(0.5)

        # Annotate: time flows left → right
        time_arrow = Arrow(LEFT * 3.5 + DOWN * 2.2, RIGHT * 3.5 + DOWN * 2.2,
                           color=QORANGE, stroke_width=3)
        time_label = Text("Time →", font_size=22, color=QORANGE).next_to(time_arrow, DOWN, buff=0.15)
        self.play(GrowArrow(time_arrow), Write(time_label))
        self.wait(0.5)

        # Add gates one by one with labels
        h_gate = qc.add_single_gate("H", 0, 1, color=QBLUE)
        h_note = Text("Hadamard", font_size=18, color=QBLUE).next_to(h_gate, UP, buff=0.3)
        self.play(FadeIn(h_gate, scale=0.5), Write(h_note))
        self.wait(0.5)

        cnot = qc.add_cnot(0, 1, 2, color=QPURPLE)
        cnot_note = Text("CNOT", font_size=18, color=QPURPLE).next_to(cnot, UP, buff=0.3)
        self.play(FadeIn(cnot, scale=0.5), Write(cnot_note))
        self.wait(0.5)

        m0 = qc.add_measurement(0, 4, color=QGREEN)
        m1 = qc.add_measurement(1, 4, color=QGREEN)
        m_note = Text("Measure", font_size=18, color=QGREEN).next_to(m0, UP, buff=0.3)
        self.play(FadeIn(m0, scale=0.5), FadeIn(m1, scale=0.5), Write(m_note))
        self.wait(1)

        self.play(FadeOut(h_note), FadeOut(cnot_note), FadeOut(m_note))
        self.wait(0.5)

        # ── Key differences callout ───────────────────────────
        self.play(FadeOut(time_arrow), FadeOut(time_label))

        diffs = VGroup(
            Text("• Wires = qubits (not electrical wires)", font_size=20, color=QWHITE),
            Text("• Gates = unitary operations (reversible!)", font_size=20, color=QWHITE),
            Text("• Time flows left → right", font_size=20, color=QWHITE),
            Text("• Measurement at the end collapses state", font_size=20, color=QWHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(DOWN, buff=0.5)

        for d in diffs:
            self.play(Write(d), run_time=0.6)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])
