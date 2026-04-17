"""1.4 - Spin & Stern-Gerlach

Teaching objective: introduce intrinsic spin as a quantum property,
the Stern-Gerlach experiment, and spin-1/2 measurement.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QWHITE, QGRAY, QGREEN, QPURPLE, QORANGE,
    STEP_PAUSE, LONG_PAUSE,
)


class SpinScene(QScene):
    def construct(self):
        self.show_title_card("Spin & Stern-Gerlach")

        # Beat 2 - What is spin?
        sec = self.show_section("Intrinsic Spin", QPURPLE)
        spin_eq = MathTex(
            r"\text{spin-}\frac{1}{2}: \quad",
            r"|{\uparrow}\rangle", r" \text{ or } ", r"|{\downarrow}\rangle",
            font_size=36,
        )
        spin_eq[1].set_color(QBLUE)
        spin_eq[3].set_color(QRED)
        spin_eq.move_to(UP * 1.5)
        self.play(Write(spin_eq), run_time=1.5)

        spin_note = Text("an intrinsic quantum property,  not classical rotation",
                         font_size=24, color=QGRAY).next_to(spin_eq, DOWN, buff=0.6)
        self.play(Write(spin_note), run_time=1.5)
        self.wait(LONG_PAUSE)
        self.fade_out_group(spin_eq, spin_note, sec)

        # Beat 3 - Stern-Gerlach apparatus
        sec2 = self.show_section("Stern-Gerlach Experiment", QORANGE)

        # Simplified apparatus
        source = VGroup(
            Circle(radius=0.3, color=QGRAY, fill_opacity=0.2),
            Text("source", font_size=18, color=QGRAY),
        ).arrange(DOWN, buff=0.2).move_to(LEFT * 4.5)

        magnet_n = Text("N", font_size=28, color=QRED, weight=BOLD).move_to(LEFT * 1 + UP * 1.5)
        magnet_s = Text("S", font_size=28, color=QBLUE, weight=BOLD).move_to(LEFT * 1 + DOWN * 1.5)
        mag_box = Rectangle(width=1.5, height=3.5, color=QGRAY, stroke_opacity=0.3
                            ).move_to(LEFT * 1)

        screen = Rectangle(width=0.15, height=3.5, color=QGRAY, fill_opacity=0.2
                           ).move_to(RIGHT * 3)

        self.play(FadeIn(source), FadeIn(mag_box), FadeIn(magnet_n), FadeIn(magnet_s),
                  FadeIn(screen), run_time=1.5)

        # Beam splits into two
        beam_in = Arrow(LEFT * 3.8, LEFT * 1.8, color=QORANGE, stroke_width=3, buff=0)
        beam_up = Arrow(LEFT * 0.2 + UP * 0.3, RIGHT * 2.8 + UP * 1.0, color=QBLUE,
                        stroke_width=3, buff=0)
        beam_down = Arrow(LEFT * 0.2 + DOWN * 0.3, RIGHT * 2.8 + DOWN * 1.0, color=QRED,
                          stroke_width=3, buff=0)

        self.play(GrowArrow(beam_in), run_time=1.2)
        self.play(GrowArrow(beam_up), GrowArrow(beam_down), run_time=1.5)

        up_dot = Dot(RIGHT * 3 + UP * 1.0, color=QBLUE, radius=0.15)
        down_dot = Dot(RIGHT * 3 + DOWN * 1.0, color=QRED, radius=0.15)
        up_lbl = MathTex(r"|{\uparrow}\rangle", font_size=24, color=QBLUE
                         ).next_to(up_dot, RIGHT, buff=0.3)
        down_lbl = MathTex(r"|{\downarrow}\rangle", font_size=24, color=QRED
                           ).next_to(down_dot, RIGHT, buff=0.3)

        self.play(FadeIn(up_dot), FadeIn(down_dot), Write(up_lbl), Write(down_lbl),
                  run_time=1.5)
        self.wait(LONG_PAUSE)

        result_note = Text("only  2  outcomes:  spin up  or  spin down",
                           font_size=24, color=QGREEN).to_edge(DOWN, buff=0.5)
        self.play(Write(result_note), run_time=1.5)
        self.play(Indicate(result_note, color=QGREEN, scale_factor=1.05))
        self.wait(LONG_PAUSE)
        self.clear_scene()

        # Beat 4 - Connection to qubits
        sec3 = self.show_section("From Spin to Qubit", QBLUE)
        connection = VGroup(
            MathTex(r"|{\uparrow}\rangle \leftrightarrow |0\rangle", font_size=36, color=QBLUE),
            MathTex(r"|{\downarrow}\rangle \leftrightarrow |1\rangle", font_size=36, color=QRED),
        ).arrange(DOWN, buff=0.6).move_to(UP * 0.5)
        self.play(Write(connection[0]), run_time=1.5)
        self.play(Write(connection[1]), run_time=1.5)

        bridge = Text("spin-1/2  systems  are  natural  qubits",
                      font_size=26, color=QGREEN).next_to(connection, DOWN, buff=0.6)
        self.play(Write(bridge))
        self.wait(LONG_PAUSE)
        self.clear_scene()
