"""2.1 - What Is a Quantum Circuit?

Teaching objective: contrast classical and quantum circuits, establish
left-to-right time flow, highlight key differences.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QWHITE, QGRAY, QGREEN, QCYAN, QORANGE,
    STEP_PAUSE, LONG_PAUSE,
)
from common.circuit import QuantumCircuit


class WhatIsACircuitScene(QScene):
    def construct(self):
        self.show_title_card("What Is a Quantum Circuit?")

        # Beat 2 - Classical circuit
        sec = self.show_section("Classical Circuit", QGRAY)
        c_wires = VGroup(
            Line(LEFT * 3, RIGHT * 0, color=QGRAY, stroke_width=2).shift(0.5 * UP),
            Line(LEFT * 3, RIGHT * 0, color=QGRAY, stroke_width=2).shift(0.5 * DOWN),
        )
        and_box = VGroup(
            Rectangle(width=1.0, height=0.8, color=QGRAY, fill_opacity=0.15),
            Text("AND", font_size=24, color=QGRAY),
        ).move_to(RIGHT * 1.5)
        out_wire = Line(RIGHT * 2, RIGHT * 3.5, color=QGRAY, stroke_width=2)
        self.play(Create(c_wires), run_time=1.2)
        self.play(FadeIn(and_box), Create(out_wire))
        self.pause()
        self.fade_out_group(c_wires, and_box, out_wire, sec)

        # Beat 3 - Quantum circuit
        sec2 = self.show_section("Quantum Circuit", QCYAN)
        qc = QuantumCircuit(num_qubits=2, num_cols=4, wire_length=6.0, labels=["0", "0"])
        qc.move_to(UP * 0.3)
        self.play(FadeIn(qc), run_time=1.5)
        h_gate = qc.add_single_gate("H", 0, 1, color=QBLUE)
        self.play(FadeIn(h_gate), run_time=1.2)
        m0 = qc.add_measurement(0, 3)
        m1 = qc.add_measurement(1, 3)
        self.play(FadeIn(m0), FadeIn(m1), run_time=1.2)
        self.pause()

        # Beat 4 - Comparison table
        rows = VGroup()
        headers = ["Feature", "Classical", "Quantum"]
        data = [
            ["Reversible?", "No", "Yes  (unitary)"],
            ["State  space", "bits", "qubits"],
            ["Output", "deterministic", "probabilistic"],
        ]
        for i, row in enumerate([headers] + data):
            cols = VGroup(*[
                Text(cell, font_size=22, color=QWHITE if i == 0 else QGRAY)
                for cell in row
            ]).arrange(RIGHT, buff=1.5)
            rows.add(cols)
        rows.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        rows.move_to(DOWN * 2.2).scale(0.9)
        self.play(FadeIn(rows, shift=UP * 0.3), run_time=1.5)
        self.play(Circumscribe(rows[0], color=QCYAN))
        self.wait(LONG_PAUSE)

        # Beat 5 - Time arrow
        self.clear_scene()
        sec3 = self.show_section("Time Flow", QCYAN)
        wire = Line(LEFT * 4.5, RIGHT * 4.5, color=QCYAN, stroke_width=2)
        time_arrow = Arrow(LEFT * 4.5, RIGHT * 4.5, color=QORANGE, buff=0).shift(DOWN)
        time_lbl = Text("time", font_size=26, color=QORANGE).next_to(time_arrow, DOWN, buff=0.25)
        self.play(Create(wire))
        self.play(GrowArrow(time_arrow), FadeIn(time_lbl, shift=UP * 0.2))
        self.wait(LONG_PAUSE)
        self.clear_scene()
