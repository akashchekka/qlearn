"""7.4 - Quantum Machine Learning

Teaching objective: feature maps, PQC classifier, training loop, caveats.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QWHITE, QGRAY, QGREEN, QORANGE, QPURPLE, QTEAL,
    STEP_PAUSE, LONG_PAUSE,
)


class QuantumMLScene(QScene):
    def construct(self):
        self.show_title_card("Quantum ML")

        # Beat 2 - Pipeline diagram
        sec = self.show_section("QML Pipeline", QBLUE)
        stages = [
            ("Data", QORANGE),
            ("U_phi(x)", QBLUE),
            ("U(theta)", QBLUE),
            ("Measure", QGREEN),
            ("Loss", QORANGE),
            ("Optimizer", QPURPLE),
        ]
        boxes = VGroup()
        for label, color in stages:
            box = VGroup(
                RoundedRectangle(width=1.4, height=0.6, color=color,
                                 fill_opacity=0.15, corner_radius=0.08),
                Text(label, font_size=18, color=color),
            )
            boxes.add(box)
        boxes.arrange(RIGHT, buff=0.5).move_to(UP * 1.5).scale(0.9)
        self.play(FadeIn(boxes), run_time=1.5)

        # Arrows
        for i in range(len(boxes) - 1):
            arrow = Arrow(boxes[i].get_right(), boxes[i+1].get_left(),
                          color=QGRAY, buff=0.05, stroke_width=2)
            self.play(GrowArrow(arrow), run_time=0.3)

        # Feedback arrow
        feedback = CurvedArrow(boxes[-1].get_bottom(), boxes[2].get_bottom(),
                               color=QPURPLE, angle=-TAU/4)
        fb_lbl = Text("update  theta", font_size=18, color=QPURPLE).next_to(feedback, DOWN, buff=0.2)
        self.play(Create(feedback), Write(fb_lbl), run_time=1.2)
        self.wait(LONG_PAUSE)
        self.fade_out_group(boxes, feedback, fb_lbl, sec)

        # Beat 4 - Three approaches
        sec2 = self.show_section("Approaches", QTEAL)
        approaches = VGroup(
            VGroup(
                RoundedRectangle(width=3.5, height=0.7, color=QTEAL, fill_opacity=0.1,
                                 corner_radius=0.1),
                Text("Variational  classifiers", font_size=22, color=QWHITE),
            ),
            VGroup(
                RoundedRectangle(width=3.5, height=0.7, color=QTEAL, fill_opacity=0.1,
                                 corner_radius=0.1),
                Text("Quantum  kernels", font_size=22, color=QWHITE),
            ),
            VGroup(
                RoundedRectangle(width=3.5, height=0.7, color=QTEAL, fill_opacity=0.1,
                                 corner_radius=0.1),
                Text("Quantum  generative  models", font_size=22, color=QWHITE),
            ),
        ).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        self.play(FadeIn(approaches), run_time=1.5)
        self.wait(LONG_PAUSE)

        # Beat 5 - Caveat
        caveat = Text("no  proven  QML  advantage  on  broad  problems  yet",
                      font_size=24, color=QORANGE).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(caveat, shift=UP))
        self.play(Circumscribe(caveat, color=QORANGE))
        self.wait(LONG_PAUSE)
        self.clear_scene()
