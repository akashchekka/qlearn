"""2.3 — Circuit Depth & Complexity (animation only)"""
from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QPURPLE, QCYAN, QORANGE, QYELLOW
from common.circuit import QuantumCircuit


class CircuitDepthScene(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        # ── Part 1: Width = number of qubits ──────────────────
        sec1 = Text("Circuit Width", font_size=32, color=QCYAN, weight=BOLD)
        sec1.to_edge(UP, buff=0.5)
        self.play(Write(sec1))

        qc_w = QuantumCircuit(num_qubits=4, num_cols=5, wire_length=6.0,
                              labels=["q_0", "q_1", "q_2", "q_3"])
        qc_w.shift(DOWN * 0.3)
        self.play(FadeIn(qc_w))

        # Brace for width
        brace = Brace(qc_w, LEFT, color=QORANGE)
        w_label = Text("Width = 4 qubits", font_size=20, color=QORANGE).next_to(brace, LEFT, buff=0.15)
        self.play(GrowFromCenter(brace), Write(w_label))
        self.wait(1.5)
        self.play(FadeOut(qc_w), FadeOut(brace), FadeOut(w_label), FadeOut(sec1))

        # ── Part 2: Depth = longest path ──────────────────────
        sec2 = Text("Circuit Depth", font_size=32, color=QCYAN, weight=BOLD)
        sec2.to_edge(UP, buff=0.5)
        self.play(Write(sec2))

        # Deep circuit: serial gates on one qubit
        qc_deep = QuantumCircuit(num_qubits=2, num_cols=7, wire_length=8.0,
                                 labels=["q_0", "q_1"])
        qc_deep.shift(DOWN * 0.3)

        # Add serial gates on q0 (depth = 5)
        gates_serial = []
        for col, name, color in [(1, "H", QBLUE), (2, "X", QRED), (3, "Z", QGREEN),
                                  (4, "S", QPURPLE), (5, "T", QORANGE)]:
            g = qc_deep.add_single_gate(name, 0, col, color=color)
            gates_serial.append(g)

        self.play(FadeIn(qc_deep))
        self.wait(0.5)

        # Highlight each column to show depth counting
        depth_counter = Text("Depth: 0", font_size=24, color=QYELLOW)
        depth_counter.to_edge(DOWN, buff=0.8)
        self.play(Write(depth_counter))

        for i, g in enumerate(gates_serial, 1):
            box = SurroundingRectangle(g, color=QYELLOW, buff=0.1, stroke_width=2)
            new_counter = Text(f"Depth: {i}", font_size=24, color=QYELLOW).to_edge(DOWN, buff=0.8)
            self.play(Create(box), Transform(depth_counter, new_counter), run_time=0.5)
            self.play(FadeOut(box), run_time=0.2)

        depth_text = Text("Depth = 5  (gates run one after another)", font_size=20,
                          color=QWHITE).to_edge(DOWN, buff=0.4)
        self.play(Transform(depth_counter, depth_text))
        self.wait(1.5)
        self.play(FadeOut(qc_deep), FadeOut(depth_counter), FadeOut(sec2))

        # ── Part 3: Parallel gates reduce depth ───────────────
        sec3 = Text("Parallelism Reduces Depth", font_size=32, color=QCYAN, weight=BOLD)
        sec3.to_edge(UP, buff=0.5)
        self.play(Write(sec3))

        # Parallel circuit: independent gates on different qubits
        qc_par = QuantumCircuit(num_qubits=3, num_cols=6, wire_length=7.0,
                                labels=["q_0", "q_1", "q_2"])
        qc_par.shift(DOWN * 0.3 + LEFT * 0.5)

        # Column 1: H on all qubits (parallel — depth 1)
        h0 = qc_par.add_single_gate("H", 0, 1, color=QBLUE)
        h1 = qc_par.add_single_gate("H", 1, 1, color=QBLUE)
        h2 = qc_par.add_single_gate("H", 2, 1, color=QBLUE)

        # Column 2: CNOT 0→1 (depth 2)
        cnot1 = qc_par.add_cnot(0, 1, 2, color=QPURPLE)
        # Column 2: gate on q2 in parallel
        rz = qc_par.add_single_gate("R_z", 2, 2, color=QORANGE)

        # Column 3: CNOT 1→2 (depth 3)
        cnot2 = qc_par.add_cnot(1, 2, 3, color=QPURPLE)

        # Measurements
        qc_par.add_measurement(0, 5, color=QGREEN)
        qc_par.add_measurement(1, 5, color=QGREEN)
        qc_par.add_measurement(2, 5, color=QGREEN)

        self.play(FadeIn(qc_par))
        self.wait(0.5)

        # Highlight parallel column
        par_box = SurroundingRectangle(
            VGroup(h0, h1, h2), color=QYELLOW, buff=0.15, stroke_width=2
        )
        par_note = Text("Parallel: same depth!", font_size=18, color=QYELLOW)
        par_note.next_to(par_box, UP, buff=0.3)
        self.play(Create(par_box), Write(par_note))
        self.wait(1.5)
        self.play(FadeOut(par_box), FadeOut(par_note))

        # Show depth count
        depth_info = VGroup(
            Text("Width = 3 qubits", font_size=20, color=QORANGE),
            Text("Depth = 4 (H → CNOT → CNOT → Measure)", font_size=20, color=QYELLOW),
            Text("Gate count = 7 gates total", font_size=20, color=QWHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).to_edge(DOWN, buff=0.4)
        self.play(*[Write(d) for d in depth_info])
        self.wait(2)
        self.play(*[FadeOut(m) for m in [qc_par, depth_info, sec3]])

        # ── Part 4: Why depth matters — decoherence budget ────
        sec4 = Text("Why Depth Matters", font_size=32, color=QCYAN, weight=BOLD)
        sec4.to_edge(UP, buff=0.5)
        self.play(Write(sec4))

        # Timeline bar showing coherence window
        timeline = Rectangle(width=10, height=0.6, color=QGRAY,
                             fill_opacity=0.1, stroke_width=2)
        timeline.move_to(UP * 0.5)

        # Coherence window
        coh_bar = Rectangle(width=10, height=0.6, color=QGREEN,
                            fill_opacity=0.15, stroke_width=0)
        coh_bar.move_to(timeline)
        coh_label = Text("Coherence time (T₂ ≈ 100 μs)", font_size=16,
                         color=QGREEN).next_to(timeline, UP, buff=0.15)

        self.play(FadeIn(timeline), FadeIn(coh_bar), Write(coh_label))
        self.wait(0.5)

        # Shallow circuit fits
        shallow = Rectangle(width=3, height=0.35, color=QBLUE,
                            fill_opacity=0.4, stroke_width=2)
        shallow.align_to(timeline, LEFT).shift(RIGHT * 0.2)
        shallow.move_to(timeline.get_center(), coor_mask=UP * 0)
        shallow.shift(LEFT * 3.3)
        s_lbl = Text("Shallow circuit ✓", font_size=16, color=QBLUE).next_to(shallow, DOWN, buff=0.15)
        self.play(FadeIn(shallow), Write(s_lbl))
        self.wait(0.5)

        # Deep circuit overflows
        deep = Rectangle(width=12, height=0.35, color=QRED,
                         fill_opacity=0.4, stroke_width=2)
        deep.align_to(timeline, LEFT).shift(RIGHT * 0.2 + DOWN * 1.5)
        d_lbl = Text("Deep circuit ✗  (exceeds coherence!)", font_size=16,
                     color=QRED).next_to(deep, DOWN, buff=0.15)
        self.play(FadeIn(deep), Write(d_lbl))
        self.wait(1.5)

        takeaway = Text(
            "Shallower circuits = less noise = better results",
            font_size=22, color=QYELLOW, weight=BOLD,
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(takeaway))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])
