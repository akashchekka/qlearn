"""4.1 - Bell States

Teaching objective: build Bell circuit, derive |Phi+>, enumerate all four.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QWHITE, QGRAY, QGREEN, QORANGE, QPURPLE,
    STEP_PAUSE, LONG_PAUSE, SMALL_MATH_SIZE,
)
from common.circuit import QuantumCircuit

EQ_X = 3.5


class BellStatesScene(QScene):
    def construct(self):
        self.show_title_card("Bell States")

        # Beat 2 - Circuit
        sec = self.show_section("Bell Circuit", QORANGE)
        qc = QuantumCircuit(num_qubits=2, num_cols=4, wire_length=6.0, labels=["0", "0"])
        qc.move_to(LEFT * 1.5 + UP * 0.5)
        self.play(FadeIn(qc), run_time=1.5)
        h = qc.add_single_gate("H", 0, 1, color=QBLUE)
        self.play(FadeIn(h), run_time=1.2)
        cnot = qc.add_cnot(0, 1, 2, color=QORANGE)
        self.play(FadeIn(cnot), run_time=1.2)
        self.pause()

        # Beat 3 - State evolution
        states = [
            r"|00\rangle",
            r"\frac{|0\rangle + |1\rangle}{\sqrt{2}} |0\rangle",
            r"\frac{|00\rangle + |11\rangle}{\sqrt{2}} = |\Phi^+\rangle",
        ]
        state_lbl = MathTex(states[0], font_size=SMALL_MATH_SIZE, color=QWHITE
                            ).move_to(DOWN * 2.0)
        self.play(Write(state_lbl), run_time=1.2)
        for s in states[1:]:
            new_lbl = MathTex(s, font_size=SMALL_MATH_SIZE, color=QWHITE).move_to(DOWN * 2.0)
            self.play(TransformMatchingTex(state_lbl, new_lbl), run_time=1.2)
            state_lbl = new_lbl
            self.pause()
        self.play(Indicate(state_lbl, color=QORANGE))

        self.wait(LONG_PAUSE)
        self.fade_out_group(qc, h, cnot, state_lbl, sec)

        # Beat 4 - Four Bell states table
        sec2 = self.show_section("Four Bell States", QORANGE)
        bell_states = VGroup(
            MathTex(r"|\Phi^+\rangle = \frac{|00\rangle+|11\rangle}{\sqrt{2}}", font_size=24, color=QWHITE),
            MathTex(r"|\Phi^-\rangle = \frac{|00\rangle-|11\rangle}{\sqrt{2}}", font_size=24, color=QWHITE),
            MathTex(r"|\Psi^+\rangle = \frac{|01\rangle+|10\rangle}{\sqrt{2}}", font_size=24, color=QWHITE),
            MathTex(r"|\Psi^-\rangle = \frac{|01\rangle-|10\rangle}{\sqrt{2}}", font_size=24, color=QWHITE),
        ).arrange(DOWN, buff=0.6, aligned_edge=LEFT).move_to(ORIGIN)
        for bs in bell_states:
            self.play(Write(bs), run_time=1.2)
        self.wait(LONG_PAUSE)
        self.clear_scene()
