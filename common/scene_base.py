"""Base scene class providing consistent structure for all lessons."""
import sys
from pathlib import Path
from manim import *
from .styles import (
    QDARK, QBLUE, QWHITE, QGRAY,
    title_card, section_title,
    TITLE_HOLD, STEP_PAUSE,
)


# Ensure project root is on sys.path so `common` is importable
# when manim renders a scene file inside a module subfolder.
_PROJECT_ROOT = str(Path(__file__).resolve().parent.parent)
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)


class QScene(Scene):
    """Base class for all quantum-computing lesson scenes.

    Subclasses only need to override ``construct``.  The helpers below
    keep title cards, section headers, and transitions consistent
    across the entire video series.
    """

    def setup(self):
        self.camera.background_color = QDARK

    # ── title card ────────────────────────────────────────────

    def show_title_card(self, topic_name: str):
        card = title_card(topic_name)
        self.play(FadeIn(card, scale=0.9), run_time=1.5)
        self.wait(TITLE_HOLD)
        self.play(FadeOut(card))
        self.wait(0.5)

    # ── section header ────────────────────────────────────────

    def show_section(self, text: str, color=QBLUE) -> Text:
        header = section_title(text, color)
        header.to_edge(UP, buff=0.5)
        self.play(Write(header))
        return header

    # ── cleanup helpers ───────────────────────────────────────

    def clear_scene(self):
        """Fade out every mobject currently on screen."""
        if self.mobjects:
            self.play(*[FadeOut(m) for m in self.mobjects])

    def fade_out_group(self, *mobjects):
        self.play(*[FadeOut(m) for m in mobjects])

    # ── brief pause after a concept ───────────────────────────

    def pause(self, duration: float = STEP_PAUSE):
        self.wait(duration)
