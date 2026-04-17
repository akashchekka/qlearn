"""7.2 - QAOA

Teaching objective: Max-Cut, layered ansatz, optimization landscape.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QWHITE, QGRAY, QGREEN, QORANGE, QPURPLE, QYELLOW,
    STEP_PAUSE, LONG_PAUSE,
)
from common.circuit import QuantumCircuit


class QAOAScene(QScene):
    def construct(self):
        self.show_title_card("QAOA")

        # Beat 2 - Graph + Max-Cut
        sec = self.show_section("Max-Cut Problem", QPURPLE)

        # 4-node graph
        positions = [UP + LEFT, UP + RIGHT, DOWN + LEFT, DOWN + RIGHT]
        colors_list = [QBLUE, QRED, QRED, QBLUE]
        dots = VGroup(*[Dot(p, color=c, radius=0.15) for p, c in zip(positions, colors_list)])
        edges = VGroup()
        edge_pairs = [(0,1),(0,2),(1,2),(1,3),(2,3)]
        for i, j in edge_pairs:
            e = Line(positions[i], positions[j], color=QGRAY, stroke_width=2)
            edges.add(e)
        graph = VGroup(edges, dots).move_to(LEFT * 3)
        self.play(FadeIn(graph), run_time=1.5)

        cut_note = Text("Max-Cut:  maximize  cut  edges", font_size=24, color=QYELLOW
                        ).move_to(RIGHT * 2.5 + UP * 1.0)
        self.play(Write(cut_note))
        self.wait(LONG_PAUSE)
        self.fade_out_group(graph, cut_note, sec)

        # Beat 3 - QAOA circuit
        sec2 = self.show_section("QAOA Circuit", QPURPLE)
        qc = QuantumCircuit(num_qubits=4, num_cols=6, wire_length=8.0,
                            labels=["0","0","0","0"])
        qc.move_to(ORIGIN)
        self.play(FadeIn(qc), run_time=1.5)

        # H layer
        for q in range(4):
            g = qc.add_single_gate("H", q, 0, color=QBLUE)
            self.play(FadeIn(g), run_time=0.2)

        # UC and UB blocks
        uc1 = qc.add_multi_qubit_gate("U_C", [0,1,2,3], 2, color=QPURPLE)
        ub1 = qc.add_multi_qubit_gate("U_B", [0,1,2,3], 3, color=QORANGE)
        self.play(FadeIn(uc1), FadeIn(ub1), run_time=1.2)

        # Measure
        for q in range(4):
            m = qc.add_measurement(q, 5)
            self.play(FadeIn(m), run_time=0.2)
        self.wait(LONG_PAUSE)

        # Beat 5 - Recap
        recap = Text("more  layers  ->  closer  to  optimum,  but  harder  to  train",
                     font_size=24, color=QGRAY).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(recap, shift=UP))
        self.play(Circumscribe(recap, color=QGRAY))
        self.wait(LONG_PAUSE)
        self.clear_scene()
