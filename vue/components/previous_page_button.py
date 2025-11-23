"""A component to display a back button."""
import reflex as rx
from vue.states.history_state import HistoryState, HistoryEntry


def previous_page_button() -> rx.Component:
    """Render a single back button."""
    return rx.link(
                rx.icon("arrow-left", size=16),
                "Back",
                href="/",
                color_scheme="gray",
                margin_bottom="16px",
            )