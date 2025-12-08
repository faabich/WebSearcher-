"""A component to display the header of the homepage."""
import reflex as rx
from vue.components.previous_page_button import previous_page_button
from vue.states.history_state import HistoryState, HistoryEntry

class NavState(rx.State):
    """A state to check the current page path."""

    @rx.var
    def is_history_page(self) -> bool:
        """Check if the current page is the history page."""
        return self.router.page.path == "/history"


def history_nav_button() -> rx.Component:
    """A button that navigates to /history from home, and to / from history."""
    return rx.cond(
        NavState.is_history_page,
        rx.link(
            rx.icon("search", size=18),
            "Back to Query",
            href="/",
        ),
        rx.link(
            rx.icon("history", size=18),
            "History",
            href="/history",
        ),
    )


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