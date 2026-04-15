"""6.4 — Quantum Machine Learning (animation only)"""
from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QPURPLE, QORANGE
from common.circuit import QuantumCircuit


class QuantumMLScene(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        # ── Classical data → Quantum encoding ─────────────────
        # Data points in 2D
        rng = np.random.default_rng(42)
        class_a = rng.normal(loc=[-1, 1], scale=0.4, size=(12, 2))
        class_b = rng.normal(loc=[1, -0.5], scale=0.4, size=(12, 2))

        axes_o = LEFT * 3 + DOWN * 0.3
        scale = 1.2

        # Axes
        x_ax = Arrow(axes_o + LEFT * 0.3, axes_o + 3 * RIGHT, color=QGRAY, buff=0, stroke_width=1.5)
        y_ax = Arrow(axes_o + DOWN * 0.3, axes_o + 3 * UP, color=QGRAY, buff=0, stroke_width=1.5)
        self.play(GrowArrow(x_ax), GrowArrow(y_ax))

        dots_a = VGroup()
        for pt in class_a:
            pos = axes_o + pt[0] * scale * RIGHT + pt[1] * scale * UP
            dots_a.add(Dot(pos, radius=0.06, color=QBLUE))
        dots_b = VGroup()
        for pt in class_b:
            pos = axes_o + pt[0] * scale * RIGHT + pt[1] * scale * UP
            dots_b.add(Dot(pos, radius=0.06, color=QRED))

        self.play(FadeIn(dots_a, lag_ratio=0.05), FadeIn(dots_b, lag_ratio=0.05))

        class_lbl = MathTex(r"\text{classical data}", font_size=22, color=QGRAY)
        class_lbl.next_to(x_ax, DOWN, buff=0.3)
        self.play(Write(class_lbl))
        self.wait(1)

        # Arrow to quantum encoding
        encode_arrow = Arrow(
            axes_o + 2.5 * RIGHT + 1.5 * UP,
            RIGHT * 2 + 1.5 * UP,
            color=QPURPLE, stroke_width=2, buff=0.2,
        )
        encode_lbl = MathTex(r"\phi(x)", font_size=22, color=QPURPLE).next_to(encode_arrow, UP, buff=0.1)
        self.play(GrowArrow(encode_arrow), Write(encode_lbl))

        # Hilbert space (abstract circles)
        hilbert = VGroup(
            Ellipse(width=3.5, height=2.5, color=QPURPLE, stroke_opacity=0.3, fill_opacity=0.05),
            MathTex(r"\mathcal{H}", font_size=28, color=QPURPLE).shift(UP * 0.8),
        ).move_to(RIGHT * 4.2 + UP * 0.8)
        self.play(FadeIn(hilbert))

        # Dots mapped into Hilbert space
        h_dots_a = VGroup()
        h_dots_b = VGroup()
        for i in range(6):
            angle = i * 0.5 + 0.3
            pos = hilbert.get_center() + 0.6 * np.array([np.cos(angle), np.sin(angle) * 0.6, 0])
            h_dots_a.add(Dot(pos, radius=0.05, color=QBLUE))
        for i in range(6):
            angle = i * 0.5 + 3.5
            pos = hilbert.get_center() + 0.8 * np.array([np.cos(angle), np.sin(angle) * 0.6, 0])
            h_dots_b.add(Dot(pos, radius=0.05, color=QRED))
        self.play(FadeIn(h_dots_a), FadeIn(h_dots_b))

        sep_note = MathTex(r"\text{separable in quantum space!}", font_size=18, color=QGREEN)
        sep_note.next_to(hilbert, DOWN, buff=0.3)
        self.play(Write(sep_note))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ── Parameterized Quantum Circuit as neural network ──
        circ = QuantumCircuit(num_qubits=3, num_cols=8, wire_length=10, labels=["x_1", "x_2", "x_3"])
        circ.move_to(0.5 * UP)
        self.play(FadeIn(circ))

        # Data encoding layer
        rx0 = circ.add_single_gate(r"R_x", 0, 1, color=QORANGE)
        rx1 = circ.add_single_gate(r"R_x", 1, 1, color=QORANGE)
        rx2 = circ.add_single_gate(r"R_x", 2, 1, color=QORANGE)
        self.play(FadeIn(rx0, scale=1.2), FadeIn(rx1, scale=1.2), FadeIn(rx2, scale=1.2))

        # Entangling layer
        cn1 = circ.add_cnot(0, 1, 3, color=QBLUE)
        cn2 = circ.add_cnot(1, 2, 3, color=QBLUE)
        self.play(FadeIn(cn1, scale=1.2), FadeIn(cn2, scale=1.2))

        # Trainable layer
        ry0 = circ.add_single_gate(r"R_y", 0, 5, color=QPURPLE)
        ry1 = circ.add_single_gate(r"R_y", 1, 5, color=QPURPLE)
        ry2 = circ.add_single_gate(r"R_y", 2, 5, color=QPURPLE)
        self.play(FadeIn(ry0, scale=1.2), FadeIn(ry1, scale=1.2), FadeIn(ry2, scale=1.2))

        # Measurement
        m0 = circ.add_measurement(0, 7, color=QGREEN)
        self.play(FadeIn(m0, scale=1.2))

        layer_labels = VGroup(
            MathTex(r"\text{encode}", font_size=16, color=QORANGE),
            MathTex(r"\text{entangle}", font_size=16, color=QBLUE),
            MathTex(r"\text{train}", font_size=16, color=QPURPLE),
        ).arrange(RIGHT, buff=2.0).next_to(circ, DOWN, buff=0.5)
        self.play(Write(layer_labels))
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ── Training loop animation ───────────────────────────
        # Loss curve decreasing
        axes_o = LEFT * 4 + DOWN * 1.0
        x_ax = Arrow(axes_o, axes_o + 8 * RIGHT, color=QGRAY, buff=0, stroke_width=2)
        y_ax = Arrow(axes_o, axes_o + 3.5 * UP, color=QGRAY, buff=0, stroke_width=2)
        x_lbl = MathTex(r"\text{epoch}", font_size=18, color=QGRAY).next_to(x_ax, DOWN, buff=0.1)
        y_lbl = MathTex(r"\text{loss}", font_size=18, color=QGRAY).next_to(y_ax, LEFT, buff=0.1)
        self.play(GrowArrow(x_ax), GrowArrow(y_ax), Write(x_lbl), Write(y_lbl))

        rng2 = np.random.default_rng(7)
        losses = []
        loss = 2.8
        for i in range(50):
            loss = loss * 0.95 + rng2.uniform(-0.05, 0.03)
            losses.append(max(loss, 0.3))

        dx = 8 / 50
        dots = VGroup()
        for i, l in enumerate(losses):
            pos = axes_o + (i + 1) * dx * RIGHT + l * UP
            dots.add(Dot(pos, radius=0.035, color=QPURPLE))
        self.play(FadeIn(dots, lag_ratio=0.04), run_time=2)
        self.wait(1)

        # Accuracy
        acc = MathTex(r"\text{Accuracy: } 92\%", font_size=26, color=QGREEN)
        acc.to_corner(UR, buff=0.6)
        self.play(Write(acc))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ── Approaches summary boxes ──────────────────────────
        approaches = VGroup()
        for name, color in [
            ("Quantum Kernels", QBLUE),
            ("PQC / QNN", QPURPLE),
            ("Q-Boltzmann", QORANGE),
            ("HHL (linear sys)", QGREEN),
        ]:
            box = VGroup(
                RoundedRectangle(width=2.6, height=1.2, corner_radius=0.12,
                                 color=color, fill_opacity=0.12, stroke_width=2),
                MathTex(r"\text{" + name + "}", font_size=18, color=color),
            )
            approaches.add(box)
        approaches.arrange_in_grid(rows=2, buff=0.5)

        for box in approaches:
            self.play(FadeIn(box, shift=UP * 0.2), run_time=0.4)
        self.wait(2)
        self.play(FadeOut(approaches))
