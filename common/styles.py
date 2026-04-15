"""Shared color palette, fonts, and styling constants for all animations."""
from manim import *

# ── Color Palette ──────────────────────────────────────────────
QBLUE = "#4FC3F7"       # |0⟩ state / primary accent
QRED = "#EF5350"        # |1⟩ state / secondary accent
QGREEN = "#66BB6A"      # measurement / success
QPURPLE = "#AB47BC"     # entanglement / phase
QORANGE = "#FFA726"     # oracle / highlight
QYELLOW = "#FFEE58"     # annotations
QDARK = "#1A1A2E"       # background
QGRAY = "#B0BEC5"       # secondary text / grid
QWHITE = "#ECEFF1"      # primary text
QCYAN = "#00E5FF"       # circuit wires

# ── Module Colors (for title cards) ───────────────────────────
MODULE_COLORS = {
    1: QBLUE,
    2: QGREEN,
    3: QPURPLE,
    4: QORANGE,
}

# ── Shared Styling ────────────────────────────────────────────
TITLE_FONT_SIZE = 48
SUBTITLE_FONT_SIZE = 32
BODY_FONT_SIZE = 28
LABEL_FONT_SIZE = 24
MATH_FONT_SIZE = 36

KET_TEX_TEMPLATE = TexTemplate()
KET_TEX_TEMPLATE.add_to_preamble(r"\usepackage{braket}")


def styled_title(text: str, color=QWHITE) -> Text:
    return Text(text, font_size=TITLE_FONT_SIZE, color=color, weight=BOLD)


def styled_subtitle(text: str, color=QGRAY) -> Text:
    return Text(text, font_size=SUBTITLE_FONT_SIZE, color=color)


def styled_body(text: str, color=QWHITE) -> Text:
    return Text(text, font_size=BODY_FONT_SIZE, color=color)


def styled_label(text: str, color=QGRAY) -> Text:
    return Text(text, font_size=LABEL_FONT_SIZE, color=color)


def ket(state: str, color=QWHITE) -> MathTex:
    return MathTex(rf"|{state}\rangle", color=color, font_size=MATH_FONT_SIZE)


def bra(state: str, color=QWHITE) -> MathTex:
    return MathTex(rf"\langle {state}|", color=color, font_size=MATH_FONT_SIZE)


def braket_tex(bra_s: str, ket_s: str, color=QWHITE) -> MathTex:
    return MathTex(
        rf"\langle {bra_s}|{ket_s}\rangle", color=color, font_size=MATH_FONT_SIZE
    )


def gate_matrix(matrix_str: str, color=QWHITE) -> MathTex:
    return MathTex(matrix_str, color=color, font_size=MATH_FONT_SIZE)


def title_card(
    module_num: int,
    module_name: str,
    lesson_num: int,
    lesson_name: str,
) -> VGroup:
    """Create a consistent title card for each lesson."""
    accent = MODULE_COLORS.get(module_num, QBLUE)
    mod_label = styled_label(f"Module {module_num}: {module_name}", color=accent)
    title = styled_title(lesson_name, color=QWHITE)
    lesson_label = styled_label(f"Lesson {lesson_num}", color=QGRAY)
    group = VGroup(mod_label, title, lesson_label).arrange(DOWN, buff=0.4)
    return group


def section_title(text: str, color=QBLUE) -> Text:
    """Small section header used within a scene."""
    return Text(text, font_size=SUBTITLE_FONT_SIZE, color=color, weight=BOLD)


def info_box(text: str, color=QBLUE, width=10) -> VGroup:
    """Rounded rectangle with centered text."""
    txt = styled_body(text, color=QWHITE)
    txt.width = min(txt.width, width - 0.6)
    box = RoundedRectangle(
        corner_radius=0.2,
        width=width,
        height=txt.height + 0.8,
        stroke_color=color,
        fill_color=color,
        fill_opacity=0.15,
    )
    return VGroup(box, txt)


def math_info_box(tex_string: str, color=QBLUE, width=10, font_size=BODY_FONT_SIZE) -> VGroup:
    """Rounded rectangle with centered MathTex (supports LaTeX / braket notation)."""
    txt = MathTex(tex_string, font_size=font_size, color=QWHITE)
    if txt.width > width - 0.6:
        txt.width = width - 0.6
    box = RoundedRectangle(
        corner_radius=0.2,
        width=width,
        height=txt.height + 0.8,
        stroke_color=color,
        fill_color=color,
        fill_opacity=0.15,
    )
    return VGroup(box, txt)
