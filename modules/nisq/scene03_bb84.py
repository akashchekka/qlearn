"""7.3 - BB84 Quantum Key Distribution

Teaching objective: BB84 protocol, basis sifting, eavesdropper detection.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QWHITE, QGRAY, QGREEN, QORANGE, QPURPLE,
    STEP_PAUSE, LONG_PAUSE,
)


class BB84Scene(QScene):
    def construct(self):
        self.show_title_card("BB84 Cryptography")

        # Beat 2 - Alice and Bob
        sec = self.show_section("Protocol", QBLUE)
        alice = Text("Alice", font_size=28, color=QBLUE).move_to(LEFT * 5 + UP * 2.8)
        bob = Text("Bob", font_size=28, color=QRED).move_to(RIGHT * 5 + UP * 2.8)
        self.play(Write(alice), Write(bob))

        # Beat 3 - Protocol table
        headers = ["Bit", "A basis", "Sent", "B basis", "Result", "Keep?"]
        data = [
            ["0", "Z", "|0>", "Z", "0", "Yes"],
            ["1", "Z", "|1>", "X", "?", "No"],
            ["1", "X", "|->", "X", "1", "Yes"],
            ["0", "X", "|+>", "Z", "?", "No"],
            ["1", "Z", "|1>", "Z", "1", "Yes"],
            ["0", "Z", "|0>", "X", "?", "No"],
        ]
        rows = VGroup()
        for i, row in enumerate([headers] + data):
            cols = VGroup(*[
                Text(c, font_size=20, color=QWHITE if i == 0 else QGRAY) for c in row
            ]).arrange(RIGHT, buff=0.6)
            rows.add(cols)
        rows.arrange(DOWN, buff=0.2, aligned_edge=LEFT).move_to(DOWN * 0.3).scale(0.85)

        for row in rows:
            self.play(FadeIn(row), run_time=0.5)
        self.pause()

        # Beat 4 - Highlight matching bases
        for i, d in enumerate(data):
            if d[5] == "Yes":
                highlight = SurroundingRectangle(rows[i + 1], color=QGREEN, buff=0.05)
                self.play(Create(highlight), run_time=0.3)
        self.wait(LONG_PAUSE)

        # Beat 5 - Eve detection note
        eve_note = Text("Eve  introduces  ~25%  detectable  errors", font_size=22,
                        color=QPURPLE).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(eve_note, shift=UP))
        self.play(Indicate(eve_note))
        self.wait(LONG_PAUSE)
        self.clear_scene()
