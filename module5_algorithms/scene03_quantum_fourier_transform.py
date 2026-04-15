"""4.3 — Quantum Fourier Transform (animation only)"""
from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QPURPLE, QORANGE
from common.circuit import QuantumCircuit


class QFTScene(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        # ── QFT equation ──────────────────────────────────────
        qft_eq = MathTex(
            r"|j\rangle \mapsto \frac{1}{\sqrt{N}}\sum_{k=0}^{N-1} e^{2\pi i jk/N} |k\rangle",
            font_size=34, color=QWHITE,
        )
        self.play(Write(qft_eq), run_time=2)
        self.wait(1)

        comparison = VGroup(
            MathTex(r"\text{Classical FFT: } O(N \log N)", font_size=28, color=QRED),
            MathTex(r"\text{Quantum QFT: } O(n^2)", font_size=28, color=QGREEN),
        ).arrange(DOWN, buff=0.4).next_to(qft_eq, DOWN, buff=0.8)
        self.play(Write(comparison), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(qft_eq), FadeOut(comparison))

        # ── Roots of unity on unit circle ─────────────────────
        n_roots = 8
        circle = Circle(radius=1.8, color=QGRAY, stroke_opacity=0.3).move_to(DOWN * 0.2)
        self.play(Create(circle))

        roots = VGroup()
        root_labels = VGroup()
        for k in range(n_roots):
            angle = 2 * np.pi * k / n_roots + np.pi / 2
            point = circle.get_center() + 1.8 * np.array([np.cos(angle), np.sin(angle), 0])
            dot = Dot(point, color=QBLUE, radius=0.08)
            lbl = MathTex(rf"\omega^{k}", font_size=18, color=QWHITE)
            lbl.next_to(dot, direction=np.array([np.cos(angle), np.sin(angle), 0]), buff=0.2)
            roots.add(dot)
            root_labels.add(lbl)

        self.play(FadeIn(roots), Write(root_labels), run_time=1.5)

        omega = MathTex(r"\omega = e^{2\pi i / N}", font_size=28, color=QPURPLE).to_corner(UR, buff=0.5)
        self.play(Write(omega))

        lines = VGroup()
        for k in range(n_roots):
            line = Line(circle.get_center(), roots[k].get_center(),
                        color=QPURPLE, stroke_opacity=0.4, stroke_width=1.5)
            lines.add(line)
            self.play(Create(line), run_time=0.12, rate_func=linear)
        self.wait(1.5)
        self.play(FadeOut(circle), FadeOut(roots), FadeOut(root_labels), FadeOut(omega), FadeOut(lines))

        # ── 3-Qubit QFT Circuit ───────────────────────────────
        circ = QuantumCircuit(num_qubits=3, num_cols=8, wire_length=10, labels=["q_0", "q_1", "q_2"])
        circ.move_to(0.3 * DOWN)
        self.play(FadeIn(circ))

        g1 = circ.add_single_gate("H", 0, 1, color=QGREEN)
        self.play(FadeIn(g1, scale=1.2))
        g2 = circ.add_controlled_gate(r"R_2", 1, 0, 2, color=QPURPLE)
        self.play(FadeIn(g2, scale=1.2))
        g3 = circ.add_controlled_gate(r"R_3", 2, 0, 3, color=QPURPLE)
        self.play(FadeIn(g3, scale=1.2))
        g4 = circ.add_single_gate("H", 1, 4, color=QGREEN)
        self.play(FadeIn(g4, scale=1.2))
        g5 = circ.add_controlled_gate(r"R_2", 2, 1, 5, color=QPURPLE)
        self.play(FadeIn(g5, scale=1.2))
        g6 = circ.add_single_gate("H", 2, 6, color=QGREEN)
        self.play(FadeIn(g6, scale=1.2))
        swap = circ.add_swap(0, 2, 7, color=QORANGE)
        self.play(FadeIn(swap, scale=1.2))

        self.wait(2)
        self.play(FadeOut(circ), FadeOut(g1), FadeOut(g2), FadeOut(g3),
                  FadeOut(g4), FadeOut(g5), FadeOut(g6), FadeOut(swap))
