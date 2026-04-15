"""6.2 — QAOA (animation only)"""
from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QPURPLE, QORANGE


class QAOAScene(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        # ── Max-Cut problem on a graph ────────────────────────
        # 5-node graph
        positions = {
            0: LEFT * 2 + UP * 1,
            1: RIGHT * 0 + UP * 1.8,
            2: RIGHT * 2 + UP * 1,
            3: RIGHT * 1.5 + DOWN * 1,
            4: LEFT * 1.5 + DOWN * 1,
        }
        edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 3)]

        nodes = VGroup()
        node_labels = VGroup()
        for i, pos in positions.items():
            dot = Dot(pos, radius=0.2, color=QGRAY, fill_opacity=0.5)
            lbl = Text(str(i), font_size=18, color=QWHITE).move_to(pos)
            nodes.add(dot)
            node_labels.add(lbl)

        edge_lines = VGroup()
        for u, v in edges:
            line = Line(positions[u], positions[v], color=QGRAY, stroke_width=2, stroke_opacity=0.4)
            edge_lines.add(line)

        graph = VGroup(edge_lines, nodes, node_labels)
        graph.move_to(ORIGIN)

        self.play(FadeIn(graph))
        self.wait(0.5)

        # Show a cut — color nodes in two groups
        group_a = [0, 2, 3]  # blue
        group_b = [1, 4]     # red

        for i in group_a:
            self.play(nodes[i].animate.set_color(QBLUE), run_time=0.2)
        for i in group_b:
            self.play(nodes[i].animate.set_color(QRED), run_time=0.2)

        # Highlight cut edges
        cut_edges = [(u, v) for u, v in edges
                     if (u in group_a) != (v in group_a)]
        for idx, (u, v) in enumerate(edges):
            if (u, v) in cut_edges or (v, u) in cut_edges:
                self.play(edge_lines[idx].animate.set_color(QORANGE).set_stroke(width=4), run_time=0.15)

        cut_count = MathTex(r"\text{Cut} = " + str(len(cut_edges)), font_size=28, color=QORANGE)
        cut_count.to_edge(DOWN, buff=0.5)
        self.play(Write(cut_count))
        self.wait(2)
        self.play(FadeOut(graph), FadeOut(cut_count))

        # ── QAOA circuit layers ───────────────────────────────
        # Layer structure: |+⟩ → (Cost layer → Mixer layer) × p → Measure
        n_qubits = 4
        layer_width = 1.2
        wire_y = [1.5 - i * 0.8 for i in range(n_qubits)]
        start_x = -5

        wires = VGroup()
        q_labels = VGroup()
        for i in range(n_qubits):
            w = Line(start_x * RIGHT + wire_y[i] * UP,
                     (start_x + 10) * RIGHT + wire_y[i] * UP,
                     color=QGRAY, stroke_width=1.5, stroke_opacity=0.4)
            wires.add(w)
            lbl = MathTex(rf"|+\rangle", font_size=18, color=QGRAY)
            lbl.next_to(w, LEFT, buff=0.2)
            q_labels.add(lbl)

        self.play(FadeIn(wires), FadeIn(q_labels))

        # Hadamard block
        x = start_x + 1.0
        h_block = VGroup()
        for i in range(n_qubits):
            box = Square(side_length=0.5, color=QGREEN, fill_opacity=0.2, stroke_width=1.5)
            box.move_to(x * RIGHT + wire_y[i] * UP)
            lbl = MathTex(r"H", font_size=16, color=QGREEN).move_to(box)
            h_block.add(box, lbl)
        self.play(FadeIn(h_block, scale=1.1))

        # Cost and mixer layers (p=2)
        layers = VGroup()
        for p in range(2):
            cx = start_x + 2.5 + p * 3.5
            # Cost layer (orange)
            cost_rect = Rectangle(
                width=1.2, height=wire_y[0] - wire_y[-1] + 0.8,
                color=QORANGE, fill_opacity=0.1, stroke_width=2,
            ).move_to(cx * RIGHT + np.mean(wire_y) * UP)
            cost_lbl = MathTex(rf"U_C", font_size=18, color=QORANGE).move_to(cost_rect)
            cost_p = MathTex(rf"\gamma_{p+1}", font_size=14, color=QORANGE).next_to(cost_rect, DOWN, buff=0.15)
            self.play(FadeIn(VGroup(cost_rect, cost_lbl, cost_p), scale=1.1), run_time=0.5)

            # Mixer layer (purple)
            mx = cx + 1.8
            mix_rect = Rectangle(
                width=1.2, height=wire_y[0] - wire_y[-1] + 0.8,
                color=QPURPLE, fill_opacity=0.1, stroke_width=2,
            ).move_to(mx * RIGHT + np.mean(wire_y) * UP)
            mix_lbl = MathTex(rf"U_M", font_size=18, color=QPURPLE).move_to(mix_rect)
            mix_p = MathTex(rf"\beta_{p+1}", font_size=14, color=QPURPLE).next_to(mix_rect, DOWN, buff=0.15)
            self.play(FadeIn(VGroup(mix_rect, mix_lbl, mix_p), scale=1.1), run_time=0.5)
            layers.add(cost_rect, cost_lbl, cost_p, mix_rect, mix_lbl, mix_p)

        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ── Optimization landscape ────────────────────────────
        axes_o = LEFT * 4 + DOWN * 0.5
        x_ax = Arrow(axes_o, axes_o + 8 * RIGHT, color=QGRAY, buff=0, stroke_width=2)
        y_ax = Arrow(axes_o, axes_o + 3.5 * UP, color=QGRAY, buff=0, stroke_width=2)
        x_lbl = MathTex(r"\gamma, \beta", font_size=18, color=QGRAY).next_to(x_ax, DOWN, buff=0.1)
        y_lbl = MathTex(r"\langle C \rangle", font_size=18, color=QGRAY).next_to(y_ax, LEFT, buff=0.1)
        self.play(GrowArrow(x_ax), GrowArrow(y_ax), Write(x_lbl), Write(y_lbl))

        # Wavy cost function
        dx = 8 / 60
        xs = np.linspace(0, 8, 60)
        ys = 1.5 + np.sin(xs * 1.2) * 0.6 + np.sin(xs * 2.5) * 0.3
        points = [axes_o + x * RIGHT + y * UP for x, y in zip(xs, ys)]
        curve = VMobject(color=QORANGE, stroke_width=2)
        curve.set_points_smoothly(points)
        self.play(Create(curve), run_time=1.5)

        # Ball rolling to maximum
        peak_idx = np.argmax(ys)
        ball = Dot(points[0], radius=0.08, color=QGREEN)
        self.play(FadeIn(ball))
        for i in range(1, peak_idx + 1, 2):
            self.play(ball.animate.move_to(points[i]), run_time=0.06, rate_func=linear)
        self.wait(0.5)

        opt_lbl = MathTex(r"\text{optimal}", font_size=20, color=QGREEN).next_to(ball, UP, buff=0.2)
        self.play(Write(opt_lbl))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])
