"""Render readable chat text without accepting model-supplied HTML."""
from markdown_it import MarkdownIt

_renderer = MarkdownIt("commonmark", {"html": False, "breaks": True}).enable("table").disable("image")


def render_markdown(text):
    return _renderer.render(text or "")
