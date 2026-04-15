"""3.2 — Quantum Teleportation (animation only)"""
from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QPURPLE, QORANGE, QYELLOW
from common.circuit import QuantumCircuit


class QuantumTeleportationScene(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        # ── Circuit ───────────────────────────────────────────
        circ = QuantumCircuit(num_qubits=3, num_cols=8, wire_length=10, labels=[r"\psi", "0", "0"])
        circ.move_to(0.3 * UP)
        self.play(FadeIn(circ))

        # Bell pair
        h_bell = circ.add_single_gate("H", 1, 1, color=QGREEN)
        self.play(FadeIn(h_bell, scale=1.2))
        cnot_bell = circ.add_cnot(1, 2, 2, color=QPURPLE)
        self.play(FadeIn(cnot_bell, scale=1.2))
        circ.add_barrier(3)
        self.wait(0.5)

        # Alice's operations
        cnot_a = circ.add_cnot(0, 1, 4, color=QBLUE)
        self.play(FadeIn(cnot_a, scale=1.2))
        h_a = circ.add_single_gate("H", 0, 5, color=QBLUE)
        self.play(FadeIn(h_a, scale=1.2))
        circ.add_barrier(6)
        self.wait(0.5)

        # Measurements
        m0 = circ.add_measurement(0, 7, color=QORANGE)
        m1 = circ.add_measurement(1, 7, color=QORANGE)
        self.play(FadeIn(m0, scale=1.2), FadeIn(m1, scale=1.2))

        # Classical lines
        m0_pos = circ.gate_position(0, 7)
        m1_pos = circ.gate_position(1, 7)
        bob_pos = circ.gate_position(2, 7) + RIGHT * 0.6
        cl0 = DashedLine(m0_pos + RIGHT * 0.4, bob_pos + UP * 0.2, color=QORANGE, stroke_width=2)
        cl1 = DashedLine(m1_pos + RIGHT * 0.4, bob_pos + DOWN * 0.1, color=QORANGE, stroke_width=2)
        self.play(Create(cl0), Create(cl1))
        self.wait(2)

        self.play(FadeOut(circ), FadeOut(h_bell), FadeOut(cnot_bell),
                  FadeOut(cnot_a), FadeOut(h_a), FadeOut(m0), FadeOut(m1),
                  FadeOut(cl0), FadeOut(cl1))

        # ── Visual story ─────────────────────────────────────
        alice = VGroup(
            RoundedRectangle(width=2.2, height=2.8, corner_radius=0.2, color=QBLUE, fill_opacity=0.15),
            MathTex(r"\text{Alice}", font_size=24, color=QBLUE).shift(UP * 1.0),
        ).move_to(LEFT * 4)
        bob = VGroup(
            RoundedRectangle(width=2.2, height=2.8, corner_radius=0.2, color=QRED, fill_opacity=0.15),
            MathTex(r"\text{Bob}", font_size=24, color=QRED).shift(UP * 1.0),
        ).move_to(RIGHT * 4)

        psi = VGroup(
            Circle(radius=0.3, color=QYELLOW, fill_opacity=0.5),
            MathTex(r"|\psi\rangle", font_size=20, color=QDARK),
        ).move_to(alice.get_center() + 0.2 * DOWN)

        self.play(FadeIn(alice), FadeIn(bob), FadeIn(psi))

        bell_line = Line(alice.get_center() + DOWN * 0.8, bob.get_center() + DOWN * 0.8,
                         color=QPURPLE, stroke_width=3)
        bell_txt = MathTex(r"|\Phi^+\rangle", font_size=20, color=QPURPLE).next_to(bell_line, DOWN, buff=0.15)
        self.play(Create(bell_line), Write(bell_txt))
        self.wait(1)

        # Measure flash
        flash = Circle(radius=0.01, color=QGREEN, fill_opacity=1).move_to(alice.get_center())
        self.play(flash.animate.scale(80).set_opacity(0), run_time=0.5)

        cl_arrow = Arrow(alice.get_right() + 0.5 * UP, bob.get_left() + 0.5 * UP,
                         color=QORANGE, buff=0.1, stroke_width=2)
        bits = MathTex(r"m_1 m_2", font_size=24, color=QORANGE).next_to(cl_arrow, UP, buff=0.15)
        self.play(GrowArrow(cl_arrow), Write(bits))
        self.wait(0.5)

        # Correction → psi at Bob
        correction = MathTex(r"X^{m_2} Z^{m_1}", font_size=28, color=QRED).move_to(bob.get_center() + 0.2 * DOWN)
        self.play(Write(correction))
        self.wait(0.5)

        psi_bob = VGroup(
            Circle(radius=0.3, color=QYELLOW, fill_opacity=0.5),
            MathTex(r"|\psi\rangle", font_size=20, color=QDARK),
        ).move_to(bob.get_center() + 0.2 * DOWN)
        self.play(FadeOut(psi), FadeOut(correction), FadeIn(psi_bob, scale=1.5))
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])
