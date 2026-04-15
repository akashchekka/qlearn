"""2.1 — Pauli Gates X, Y, Z (animation only)"""
from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QPURPLE, QORANGE
from common.quantum import BlochSphere


class PauliGatesScene(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        for name, matrix_str, effect_str, color, b_start, b_end in [
            ("X",
             r"X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}",
             r"X|0\rangle = |1\rangle \quad X|1\rangle = |0\rangle",
             QRED, (0, 0), (np.pi, 0)),
            ("Y",
             r"Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}",
             r"Y|0\rangle = i|1\rangle \quad Y|1\rangle = -i|0\rangle",
             QGREEN, (0, 0), (np.pi, np.pi)),
            ("Z",
             r"Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}",
             r"Z|0\rangle = |0\rangle \quad Z|1\rangle = -|1\rangle",
             QBLUE, (np.pi / 2, 0), (np.pi / 2, np.pi)),
        ]:
            # Gate title
            gate_title = Text(f"{name} Gate", font_size=32, color=color, weight=BOLD)
            gate_title.to_edge(UP, buff=0.4)
            self.play(Write(gate_title))

            # Matrix + effect — positioned on the right with vertical spacing
            mat = MathTex(matrix_str, font_size=34, color=color).move_to(RIGHT * 3 + UP * 0.3)
            eff = MathTex(effect_str, font_size=28, color=QWHITE).move_to(RIGHT * 3 + DOWN * 1.2)

            # Bloch sphere rotation
            bloch = BlochSphere(radius=1.3, theta=b_start[0], phi=b_start[1])
            bloch.move_to(LEFT * 3)

            # Rotation axis label
            axis_lbl = MathTex(
                rf"\pi \text{{ rotation around }} {name}\text{{-axis}}",
                font_size=22, color=QGRAY,
            ).next_to(bloch, DOWN, buff=0.5)

            self.play(Write(mat), Write(eff), FadeIn(bloch, scale=0.8), Write(axis_lbl))
            self.wait(0.5)
            self.play(bloch.animate_to_state(b_end[0], b_end[1]), run_time=2)
            self.wait(1)
            self.play(FadeOut(mat), FadeOut(eff), FadeOut(bloch),
                      FadeOut(gate_title), FadeOut(axis_lbl))

        # ── Summary row: X, Y, Z gate boxes ──────────────────
        gates_row = VGroup()
        for name, color in [("X", QRED), ("Y", QGREEN), ("Z", QBLUE)]:
            box = VGroup(
                Square(side_length=1.0, color=color, fill_opacity=0.2, stroke_width=2),
                MathTex(name, font_size=36, color=color),
            )
            gates_row.add(box)
        gates_row.arrange(RIGHT, buff=1.5)
        self.play(FadeIn(gates_row, shift=UP * 0.3))
        self.wait(2)
        self.play(FadeOut(gates_row))
