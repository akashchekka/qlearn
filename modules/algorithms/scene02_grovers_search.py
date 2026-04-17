"""5.2 - Grover's Search

Teaching objective: amplitude amplification and geometric view.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QWHITE, QGRAY, QGREEN, QORANGE, QPURPLE, QYELLOW,
    STEP_PAUSE, LONG_PAUSE,
)

N_ITEMS = 8
TARGET = 3
BAR_W = 0.5
BAR_MAX_H = 3.0
BAR_BASELINE = -1.5
BAR_LABEL_Y = BAR_BASELINE - 0.3


class GroversSearchScene(QScene):
    def construct(self):
        self.show_title_card("Grover's Search")

        sec = self.show_section("Amplitude Amplification", QORANGE)

        # Beat 2 - Database
        items = VGroup(*[
            Square(side_length=0.5, color=QORANGE if i == TARGET else QGRAY,
                   fill_opacity=0.3 if i == TARGET else 0.1)
            for i in range(N_ITEMS)
        ]).arrange(RIGHT, buff=0.15).move_to(UP * 2.5)
        self.play(FadeIn(items), run_time=1.2)
        self.pause()

        # Beat 3 - Amplitude bars
        amps = np.ones(N_ITEMS) / np.sqrt(N_ITEMS)

        def make_bars(amplitudes):
            bars = VGroup()
            for i, a in enumerate(amplitudes):
                h = max(abs(a) * BAR_MAX_H, 0.01)
                color = QORANGE if i == TARGET else QGRAY
                bar = Rectangle(width=BAR_W, height=h, fill_color=color,
                                fill_opacity=0.7, stroke_width=0)
                x = (i - N_ITEMS / 2 + 0.5) * (BAR_W + 0.1)
                bar.move_to(np.array([x, BAR_BASELINE + h / 2, 0]))
                bars.add(bar)
            return bars

        bars = make_bars(amps)
        self.play(FadeIn(bars), run_time=1.2)
        self.pause()

        # Beat 4/5 - Two Grover iterations
        for iteration in range(2):
            # Oracle: flip target
            amps[TARGET] *= -1
            new_bars = make_bars(amps)
            self.play(*[Transform(bars[i], new_bars[i]) for i in range(N_ITEMS)], run_time=0.8)
            self.pause()

            # Diffusion: inversion about mean
            mean_val = np.mean(amps)
            amps = 2 * mean_val - amps
            new_bars = make_bars(amps)
            self.play(*[Transform(bars[i], new_bars[i]) for i in range(N_ITEMS)], run_time=0.8)
            self.pause()

        self.wait(LONG_PAUSE)

        # Beat 7 - Optimal count
        opt = MathTex(r"\text{optimal iterations} \approx \frac{\pi}{4}\sqrt{N}",
                      font_size=28, color=QPURPLE).to_edge(DOWN, buff=0.5)
        self.play(Write(opt))
        self.play(Indicate(opt))
        self.wait(LONG_PAUSE)
        self.clear_scene()
