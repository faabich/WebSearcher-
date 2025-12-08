"""A component to display a single special operators card."""
import reflex as rx

from vue.ddgs.ddgs import DuckDuckGoSearch

ddgs = DuckDuckGoSearch()

def query_card() -> rx.Component:
    """Render a single special operators card."""
    return rx.card(
        rx.flex(
            rx.box(
                rx.heading("Requête générée", size="3")
            )
        ),
        rx.flex(
            rx.box(
                rx.flex(
                    rx.input(),
                    spacing="2",
                    align="center",
                )
            ),
            rx.box(
                rx.flex(
                    rx.button("Rechercher", size="1"),
                    on_click=ddgs.launch_web_search(),
                    spacing="2",
                    align="center",
                )
            ),
            spacing="2",
            width="100",
            flex_wrap="wrap"
        ),
        width="100%",
    )
