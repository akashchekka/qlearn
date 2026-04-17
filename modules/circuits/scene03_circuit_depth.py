"""2.3 - Circuit Depth & Complexity

Teaching objective: define width, depth, connect depth to decoherence.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QWHITE, QGRAY, QCYAN, QPURPLE, QORANGE,
    STEP_PAUSE, LONG_PAUSE,
)
from common.circuit import QuantumCircuit


class CircuitDepthScene(QScene):
    def construct(self):
        self.show_title_card("Circuit Depth & Complexity")

        sec = self.show_section("Width & Depth", QCYAN)

        qc = QuantumCircuit(num_qubits=4, num_cols=6, wire_length=8.0,
                            labels=["0", "0", "0", "0"])
        qc.move_to(UP * 0.5)
        self.play(FadeIn(qc), run_time=1.5)

        # Add gates in layers
        for col in [1, 2, 3, 4]:
            gates = []
            for q in range(4):
                if (col + q) % 2 == 0:
                    g = qc.add_single_gate("H" if col % 2 == 1 else "X", q, col, color=QBLUE)
                    gates.append(g)
            if gates:
                self.play(*[FadeIn(g) for g in gates], run_time=0.5)

        self.pause()

        # Braces
        width_brace = Brace(qc, LEFT, color=QBLUE)
        width_lbl = Text("width = 4", font_size=24, color=QBLUE).next_to(width_brace, LEFT, buff=0.2)
        depth_brace = Brace(qc, DOWN, color=QPURPLE)
        depth_lbl = Text("depth", font_size=24, color=QPURPLE).next_to(depth_brace, DOWN, buff=0.2)

        self.play(Create(width_brace), Write(width_lbl), run_time=1.2)
        self.play(Create(depth_brace), Write(depth_lbl), run_time=1.2)
        self.wait(LONG_PAUSE)

        fidelity_note = MathTex(r"F = e^{-d/d_c}", font_size=32, color=QORANGE).to_edge(DOWN, buff=0.5)
        fidelity_lbl = Text("deeper circuit  =  more decoherence", font_size=22, color=QGRAY
                            ).next_to(fidelity_note, DOWN, buff=0.25)
        self.play(Write(fidelity_note), FadeIn(fidelity_lbl, shift=UP * 0.2), run_time=1.5)
        self.play(Indicate(fidelity_note, color=QORANGE))
        self.wait(LONG_PAUSE)
        self.clear_scene()
