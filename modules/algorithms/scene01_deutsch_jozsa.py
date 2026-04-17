"""5.1 - Deutsch-Jozsa Algorithm

Teaching objective: constant vs balanced, circuit, exponential speedup.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QWHITE, QGRAY, QGREEN, QORANGE,
    STEP_PAUSE, LONG_PAUSE, SMALL_MATH_SIZE,
)
from common.circuit import QuantumCircuit


class DeutschJozsaScene(QScene):
    def construct(self):
        self.show_title_card("Deutsch-Jozsa Algorithm")

        # Beat 2 - Problem
        sec = self.show_section("Problem", QORANGE)
        problem = MathTex(r"f: \{0,1\}^n \to \{0,1\}", font_size=32, color=QWHITE
                          ).move_to(UP * 2.0)
        q_label = Text("Is  f  constant  or  balanced?", font_size=26, color=QGRAY
                       ).next_to(problem, DOWN, buff=0.5)
        self.play(Write(problem), FadeIn(q_label, shift=UP * 0.3))
        self.wait(LONG_PAUSE)
        self.fade_out_group(problem, q_label, sec)

        # Beat 3 - Circuit (n=2)
        sec2 = self.show_section("DJ Circuit", QORANGE)
        qc = QuantumCircuit(num_qubits=3, num_cols=6, wire_length=8.0,
                            labels=["0", "0", "1"])
        qc.move_to(UP * 0.3)
        self.play(FadeIn(qc), run_time=1.5)

        # H on all
        for q in range(3):
            g = qc.add_single_gate("H", q, 1, color=QBLUE)
            self.play(FadeIn(g), run_time=0.4)

        # Oracle block
        oracle = qc.add_multi_qubit_gate("U_f", [0, 1, 2], 3, color=QORANGE)
        self.play(FadeIn(oracle), run_time=1.2)

        # H on top 2
        for q in range(2):
            g = qc.add_single_gate("H", q, 4, color=QBLUE)
            self.play(FadeIn(g), run_time=0.4)

        # Measure top 2
        for q in range(2):
            m = qc.add_measurement(q, 5)
            self.play(FadeIn(m), run_time=0.4)
        self.wait(LONG_PAUSE)

        # Beat 5 - Outcome rule
        rule = Text("all  zeros => constant,  otherwise => balanced",
                    font_size=24, color=QGREEN).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(rule, shift=UP * 0.3))
        self.play(Indicate(rule))
        self.wait(LONG_PAUSE)

        # Beat 6 - Speedup
        self.clear_scene()
        sec3 = self.show_section("Speedup", QRED)
        speedup = VGroup(
            Text("Classical:  2^(n-1) + 1  queries", font_size=26, color=QGRAY),
            Text("Quantum:  1  query", font_size=26, color=QRED),
        ).arrange(DOWN, buff=0.6).move_to(ORIGIN)
        self.play(Write(speedup[0]), run_time=1.2)
        self.play(Write(speedup[1]), run_time=1.2)
        self.play(Circumscribe(speedup, color=QRED))
        self.play(Indicate(speedup[1]))
        self.wait(LONG_PAUSE)
        self.clear_scene()
