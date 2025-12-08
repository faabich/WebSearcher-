"""A component to display the header of the homepage."""
import reflex as rx
from vue.components.previous_page_button import previous_page_button
from vue.states.history_state import HistoryState, HistoryEntry

def homepage_header() -> rx.Component:
    """Render a single history entry card."""
    return rx.flex(
        rx.vstack(
            rx.hstack(
                rx.icon("globe"),
                rx.heading("Web Search++", as_="h1"),
                align="center",
                justify="center",
                width="100%",
            ),
            rx.heading("Construisez des requêtes de recherche complexes")
        )
    )