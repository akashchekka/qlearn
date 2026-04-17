"""6.2 - Error Correction

Teaching objective: no-cloning, 3-qubit bit-flip code, surface code teaser.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QWHITE, QGRAY, QGREEN, QPURPLE,
    STEP_PAUSE, LONG_PAUSE, SMALL_MATH_SIZE,
)
from common.circuit import QuantumCircuit


class ErrorCorrectionScene(QScene):
    def construct(self):
        self.show_title_card("Error Correction")

        # Beat 2 - No-cloning
        sec = self.show_section("No-Cloning Theorem", QRED)
        noclone = MathTex(r"|\psi\rangle \to |\psi\rangle|\psi\rangle",
                          font_size=36, color=QRED).move_to(UP * 0.5)
        cross = Text("X", font_size=72, color=QRED, weight=BOLD).move_to(noclone)
        note = Text("cannot  copy  unknown  quantum  states", font_size=24, color=QGRAY
                    ).next_to(noclone, DOWN, buff=0.5)
        self.play(Write(noclone))
        self.play(FadeIn(cross, scale=2))
        self.play(Indicate(cross))
        self.play(FadeIn(note, shift=UP * 0.3))
        self.wait(LONG_PAUSE)
        self.fade_out_group(noclone, cross, note, sec)

        # Beat 3 - Bit-flip code circuit
        sec2 = self.show_section("3-Qubit Bit-Flip Code", QBLUE)
        qc = QuantumCircuit(num_qubits=3, num_cols=5, wire_length=7.0,
                            labels=["\\psi", "0", "0"])
        qc.move_to(UP * 0.3)
        self.play(FadeIn(qc), run_time=1.5)

        # Encode with CNOTs
        cn1 = qc.add_cnot(0, 1, 1, color=QBLUE)
        cn2 = qc.add_cnot(0, 2, 2, color=QBLUE)
        self.play(FadeIn(cn1), FadeIn(cn2), run_time=1.2)
        enc_note = Text("encode", font_size=20, color=QGRAY).next_to(cn1, UP, buff=0.5)
        self.play(Write(enc_note))
        self.pause()

        # Error injection
        err = qc.add_single_gate("X", 1, 3, color=QRED)
        err_note = Text("error!", font_size=20, color=QRED).next_to(err, UP, buff=0.5)
        self.play(FadeIn(err), Write(err_note), run_time=1.2)
        self.pause()

        # Correction
        corr_note = Text("syndrome  ->  correct", font_size=20, color=QGREEN).to_edge(DOWN, buff=0.5)
        self.play(Write(corr_note))
        self.wait(LONG_PAUSE)
        self.fade_out_group(qc, cn1, cn2, enc_note, err, err_note, corr_note, sec2)

        # Beat 4 - Limitation
        sec3 = self.show_section("Limitations", QGRAY)
        limit = Text("corrects  1  bit-flip  only;  real  codes  handle  phase  too",
                     font_size=24, color=QGRAY).move_to(ORIGIN)
        self.play(Write(limit))
        self.play(Indicate(limit))
        self.wait(LONG_PAUSE)
        self.clear_scene()
