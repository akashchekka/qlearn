"""6.3 - Hardware Platforms

Teaching objective: compare superconducting, trapped ions, photonic.
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


class HardwarePlatformsScene(QScene):
    def construct(self):
        self.show_title_card("Hardware Platforms")

        platforms = [
            ("Superconducting", QBLUE, "transmon  qubits,  ~ns  gates,  limited  connectivity"),
            ("Trapped Ions", QORANGE, "ion  chain,  ~us  gates,  all-to-all  connectivity"),
            ("Photonic", QPURPLE, "photon  paths,  fast  ops,  hard  two-qubit  gates"),
        ]

        for name, color, desc in platforms:
            sec = self.show_section(name, color)
            icon = VGroup(
                RoundedRectangle(width=2.0, height=1.5, color=color, fill_opacity=0.1,
                                 corner_radius=0.15),
                Text("schematic", font_size=18, color=QGRAY),
            ).move_to(LEFT * 3 + UP * 0.5)
            desc_text = Text(desc, font_size=24, color=QWHITE).move_to(RIGHT * 1.5 + UP * 0.5)
            desc_text.width = min(desc_text.width, 6.0)
            self.play(FadeIn(icon), Write(desc_text), run_time=1.5)
            self.wait(LONG_PAUSE)
            self.fade_out_group(icon, desc_text, sec)

        # Comparison table
        sec_t = self.show_section("Comparison", QGRAY)
        headers = ["Platform", "Gate Speed", "Connectivity"]
        data = [
            ["Superconducting", "~ns", "nearest-neighbor"],
            ["Trapped Ions", "~us", "all-to-all"],
            ["Photonic", "~ps", "configurable"],
        ]
        rows = VGroup()
        for i, row in enumerate([headers] + data):
            cols = VGroup(*[
                Text(c, font_size=22, color=QWHITE if i == 0 else QGRAY) for c in row
            ]).arrange(RIGHT, buff=1.0)
            rows.add(cols)
        rows.arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(ORIGIN)
        for row in rows:
            self.play(FadeIn(row), run_time=0.5)
        self.wait(LONG_PAUSE)
        self.clear_scene()
