"""1.3 - Uncertainty Principle

Teaching objective: explain Heisenberg's uncertainty principle as a
fundamental limit, not a measurement flaw.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QWHITE, QGRAY, QGREEN, QPURPLE, QORANGE, QYELLOW,
    STEP_PAUSE, LONG_PAUSE,
)


class UncertaintyPrincipleScene(QScene):
    def construct(self):
        self.show_title_card("Uncertainty Principle")

        # Beat 2 - The equation
        sec = self.show_section("Heisenberg's Limit", QPURPLE)
        heisenberg = MathTex(
            r"\Delta x \cdot \Delta p \geq \frac{\hbar}{2}",
            font_size=48, color=QWHITE,
        ).move_to(UP * 1.5)
        self.play(Write(heisenberg), run_time=2.0)

        meaning = Text("you cannot know both  position  and  momentum  precisely",
                       font_size=24, color=QGRAY).next_to(heisenberg, DOWN, buff=0.6)
        self.play(Write(meaning), run_time=1.5)
        self.wait(LONG_PAUSE)
        self.fade_out_group(heisenberg, meaning, sec)

        # Beat 3 - Narrow position = wide momentum
        sec2 = self.show_section("Position vs Momentum", QBLUE)
        axes = Axes(x_range=[-4, 4, 1], y_range=[0, 1.2, 0.5],
                    x_length=4.2, y_length=2.5,
                    axis_config={"color": QGRAY}).move_to(LEFT * 3.3)
        x_lbl = axes.get_x_axis_label(MathTex("x", font_size=22, color=QGRAY))

        narrow = axes.plot(lambda x: np.exp(-2 * x**2), x_range=[-4, 4],
                           color=QBLUE, stroke_width=3)
        narrow_lbl = Text("narrow  position", font_size=20, color=QBLUE
                          ).next_to(axes, DOWN, buff=0.5)

        self.play(Create(axes), Write(x_lbl), run_time=1.5)
        self.play(Create(narrow), Write(narrow_lbl), run_time=2.0)
        self.pause()

        # Corresponding wide momentum
        axes2 = Axes(x_range=[-4, 4, 1], y_range=[0, 1.2, 0.5],
                     x_length=4.2, y_length=2.5,
                     axis_config={"color": QGRAY}).move_to(RIGHT * 3.3)
        p_lbl = axes2.get_x_axis_label(MathTex("p", font_size=22, color=QGRAY))

        wide = axes2.plot(lambda x: np.exp(-0.1 * x**2), x_range=[-4, 4],
                          color=QRED, stroke_width=3)
        wide_lbl = Text("wide  momentum", font_size=20, color=QRED
                        ).next_to(axes2, DOWN, buff=0.5)

        self.play(Create(axes2), Write(p_lbl), run_time=1.5)
        self.play(Create(wide), Write(wide_lbl), run_time=2.0)
        self.wait(LONG_PAUSE)
        self.fade_out_group(axes, x_lbl, narrow, narrow_lbl,
                            axes2, p_lbl, wide, wide_lbl, sec2)

        # Beat 4 - Not a measurement flaw
        sec3 = self.show_section("Key Point", QGREEN)
        key = VGroup(
            Text("NOT  a limitation of our instruments", font_size=26, color=QRED),
            Text("A fundamental property of nature", font_size=26, color=QGREEN),
        ).arrange(DOWN, buff=0.6).move_to(ORIGIN)
        cross = Line(key[0].get_left(), key[0].get_right(), color=QRED, stroke_width=3)
        self.play(Write(key[0]))
        self.play(Create(cross))
        self.play(Write(key[1]))
        self.wait(LONG_PAUSE)
        self.clear_scene()
