"""4.3 - Superdense Coding

Teaching objective: send 2 classical bits using 1 qubit + entanglement.
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


class SuperdenseCodingScene(QScene):
    def construct(self):
        self.show_title_card("Superdense Coding")

        # Beat 2 - Shared Bell pair
        sec = self.show_section("Shared Entanglement", QORANGE)
        bell = MathTex(r"|\Phi^+\rangle = \frac{|00\rangle+|11\rangle}{\sqrt{2}}",
                       font_size=SMALL_MATH_SIZE, color=QORANGE).move_to(UP * 2.0)
        alice = Text("Alice", font_size=24, color=QBLUE).move_to(LEFT * 4 + UP * 0.5)
        bob = Text("Bob", font_size=24, color=QRED).move_to(RIGHT * 4 + UP * 0.5)
        self.play(Write(bell), Write(alice), Write(bob))
        self.pause()

        # Beat 3 - Encoding table
        enc_data = [
            ["Bits", "Gate"],
            ["00", "I"],
            ["01", "X"],
            ["10", "Z"],
            ["11", "XZ"],
        ]
        rows = VGroup()
        for i, row in enumerate(enc_data):
            cols = VGroup(*[
                Text(c, font_size=24, color=QWHITE if i == 0 else QGRAY) for c in row
            ]).arrange(RIGHT, buff=1.5)
            rows.add(cols)
        rows.arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to(DOWN * 0.8)
        self.play(FadeIn(rows), run_time=1.5)
        self.wait(LONG_PAUSE)
        self.fade_out_group(bell, alice, bob, rows, sec)

        # Beat 5 - Recap
        sec2 = self.show_section("Key Insight", QGREEN)
        recap = Text("1  qubit  +  prior  entanglement  =  2  classical  bits",
                     font_size=26, color=QGREEN).move_to(ORIGIN)
        self.play(Write(recap), run_time=1.5)
        self.play(Indicate(recap, color=QORANGE))
        self.wait(LONG_PAUSE)
        self.clear_scene()
