"""The dashboard page."""

import reflex as rx
from vue.components.homepage_header import homepage_header
from vue.components.special_operators_card import special_operators_card
from vue.components.query_card import query_card



@rx.page("/", title="Home - WebSearch++")
def dashboard() -> rx.Component:
    """The homepage.

    Returns:
        The UI for the homepage.

    """
    return rx.container(
        rx.flex(
            homepage_header(),
            justify="center",
            width="100%",
        ),
        rx.flex(
            rx.vstack(
                special_operators_card(),
                query_card()
            ),
            justify="center",
            width="100%"
        )
    )