"""7.1 - Variational Quantum Eigensolver (VQE)

Teaching objective: hybrid loop, ansatz, energy convergence.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QWHITE, QGRAY, QGREEN, QORANGE, QTEAL,
    STEP_PAUSE, LONG_PAUSE,
)


class VQEScene(QScene):
    def construct(self):
        self.show_title_card("VQE")

        # Beat 2 - Loop diagram
        sec = self.show_section("Hybrid Loop", QTEAL)
        nodes = [
            (UP * 1.5, "ansatz  |psi(t)>", QBLUE),
            (RIGHT * 3, "measure <H>", QBLUE),
            (DOWN * 1.5, "optimizer", QORANGE),
            (LEFT * 3, "update theta", QORANGE),
        ]
        node_mobs = VGroup()
        for pos, label, color in nodes:
            box = VGroup(
                RoundedRectangle(width=2.2, height=0.7, color=color, fill_opacity=0.15,
                                 corner_radius=0.1),
                Text(label, font_size=20, color=color),
            ).move_to(pos)
            node_mobs.add(box)
        self.play(FadeIn(node_mobs), run_time=1.5)

        # Arrows
        for i in range(4):
            start = node_mobs[i].get_center()
            end = node_mobs[(i + 1) % 4].get_center()
            arrow = Arrow(start, end, color=QGRAY, buff=0.6, stroke_width=2)
            self.play(GrowArrow(arrow), run_time=0.5)
        self.wait(LONG_PAUSE)
        self.clear_scene()

        # Beat 4 - Energy convergence
        sec2 = self.show_section("Energy Convergence", QTEAL)
        axes = Axes(x_range=[0, 10, 2], y_range=[-2, 1, 0.5],
                    x_length=6, y_length=3, axis_config={"color": QGRAY})
        axes.move_to(ORIGIN)
        x_lbl = axes.get_x_axis_label(Text("iteration", font_size=22, color=QGRAY))
        y_lbl = axes.get_y_axis_label(Text("<H>", font_size=22, color=QGRAY))
        self.play(Create(axes), Write(x_lbl), Write(y_lbl), run_time=1.5)

        # Target line
        target = DashedLine(
            axes.c2p(0, -1.5), axes.c2p(10, -1.5),
            color=QGREEN, stroke_width=2,
        )
        target_lbl = MathTex("E_0", font_size=24, color=QGREEN).next_to(
            axes.c2p(10, -1.5), RIGHT, buff=0.15)
        self.play(Create(target), Write(target_lbl))

        # Convergence curve (approaches from above)
        curve = axes.plot(lambda x: -1.5 + 2.0 * np.exp(-0.4 * x), x_range=[0, 10],
                          color=QTEAL, stroke_width=3)
        self.play(Create(curve), run_time=2.5)
        self.play(Indicate(target_lbl))
        self.wait(LONG_PAUSE)
        self.clear_scene()
