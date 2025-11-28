"""A component to display the header of the homepage."""
import reflex as rx
from vue.states.history_state import HistoryState, HistoryEntry



def homepage_header() -> rx.Component:
    """Render a single history entry card."""
    return rx.flex(
        rx.vstack(
            rx.hstack(
                rx.icon("globe"),
                rx.heading("WebSearch++", as_="h1")
            ),
            rx.heading("Construisez des requêtes de recherche complexes"),
            rx.hstack(

            )
        )
    )