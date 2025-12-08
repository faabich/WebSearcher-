"""A component to display a back button."""
import reflex as rx
from vue.states.history_state import HistoryState, HistoryEntry
from typing import Callable


def previous_page_button(on_click_handler: Callable) -> rx.Component:
    """Render a single back button."""
    return rx.button(
                rx.icon("arrow-left", size=16),
                "Back",
                color_scheme="gray",
                margin_bottom="16px",
                on_click=on_click_handler,
            )