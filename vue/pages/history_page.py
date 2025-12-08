"""The history page."""

import reflex as rx
from vue.states.history_state import HistoryState
from vue.components.history_card import history_entry_card
from vue.components.previous_page_button import previous_page_button



@rx.page("/history", title="History - WebSearch++")
def history_page() -> rx.Component:
    """The history page.

    Returns:
        The UI for the history page.
    """
    return rx.container(
        rx.flex(
            previous_page_button(on_click_handler=HistoryState.go_back),
            rx.flex(
                rx.flex(
                    rx.icon("history", size=32, color_scheme="blue"),
                    rx.vstack(
                        rx.heading("Search History", size="6"),
                        rx.text(
                            HistoryState.history.length(), " saved searches",
                            color_scheme="gray",
                        ),
                        spacing="0",
                        align="start",
                    ),
                    spacing="3",
                    align="center",
                ),
                rx.button(
                    "Clear All",
                    rx.icon("trash-2", size=16),
                    on_click=HistoryState.clear_history,
                    color_scheme="red",
                    variant="soft",
                ),
                justify="between",
                align="center",
                width="100%",
            ),
            rx.cond(
                HistoryState.history.length() > 0,
                rx.vstack(
                    rx.foreach(
                        HistoryState.history,
                        history_entry_card,
                    ),
                    spacing="4",
                    width="100%",
                    margin_top="24px",
                ),
                rx.card(
                    rx.flex(
                        rx.icon("history", size=64, color="var(--gray-6)"),
                        rx.heading("No History", size="5"),
                        rx.text("Your searches will appear here.", color_scheme="gray"),
                        direction="column",
                        spacing="4",
                        align="center",
                        padding_y="32px",
                    ),
                    width="100%",
                    margin_top="24px",
                ),
            ),
            direction="column",
            width="100%",
        ),
        size="4",
        padding="32px",
    )