"""A component to display a query generation card."""
import reflex as rx

from vue.states.home_state import HomeState

def query_card() -> rx.Component:
    """Render a heading and a responsive input in a card."""
    return rx.card(
        rx.flex(
            rx.box(
                rx.heading("Requête générée", size="3")
            ),
            direction="column"
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
                    on_click=HomeState.check_values,
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
