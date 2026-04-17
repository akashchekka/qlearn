"""5.4 - Shor's Algorithm

Teaching objective: factoring via period finding, high-level circuit.
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


class ShorsAlgorithmScene(QScene):
    def construct(self):
        self.show_title_card("Shor's Algorithm")

        # Beat 2 - Problem
        sec = self.show_section("Factoring Problem", QORANGE)
        problem = MathTex(r"N = p \times q", font_size=36, color=QWHITE).move_to(UP * 1.5)
        example = Text("Example:  N = 15 = 3 × 5", font_size=26, color=QGRAY
                       ).next_to(problem, DOWN, buff=0.6)
        self.play(Write(problem), FadeIn(example, shift=UP * 0.3))
        self.wait(LONG_PAUSE)
        self.fade_out_group(problem, example, sec)

        # Beat 3 - Reduction
        sec2 = self.show_section("Period Finding", QORANGE)
        reduction = MathTex(r"f(x) = a^x \mod N", font_size=32, color=QWHITE).move_to(UP * 1.5)
        period_note = Text("find  period  r  of  f(x)", font_size=26, color=QGRAY
                           ).next_to(reduction, DOWN, buff=0.5)
        self.play(Write(reduction), FadeIn(period_note, shift=UP * 0.3))
        self.wait(LONG_PAUSE)
        self.fade_out_group(reduction, period_note, sec2)

        # Beat 5 - High-level circuit
        sec3 = self.show_section("Circuit", QBLUE)
        qc = QuantumCircuit(num_qubits=2, num_cols=5, wire_length=8.0,
                            labels=["input", "work"])
        qc.move_to(UP * 0.3)
        self.play(FadeIn(qc), run_time=1.5)

        hn = qc.add_multi_qubit_gate("H^n", [0], 1, color=QBLUE)
        uf = qc.add_multi_qubit_gate("U_f", [0, 1], 2, color=QORANGE)
        qft = qc.add_multi_qubit_gate("QFT^{-1}", [0], 3, color=QBLUE)
        meas = qc.add_measurement(0, 4)
        for g in [hn, uf, qft, meas]:
            self.play(FadeIn(g), run_time=0.6)
        self.wait(LONG_PAUSE)

        # Beat 7 - Speedup
        speedup = VGroup(
            MathTex(r"O((\log N)^3)", font_size=28, color=QRED),
            Text("vs", font_size=24, color=QGRAY),
            MathTex(r"\sim \exp((\log N)^{1/3})", font_size=28, color=QGRAY),
        ).arrange(RIGHT, buff=0.5).to_edge(DOWN, buff=0.5)
        self.play(Write(speedup[0]), Write(speedup[1]), Write(speedup[2]))
        self.play(Circumscribe(speedup, color=QRED))
        self.play(Indicate(speedup[0]))
        self.wait(LONG_PAUSE)
        self.clear_scene()
