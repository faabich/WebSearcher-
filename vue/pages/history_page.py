"""The history page."""

import reflex as rx

@rx.page("/history", title="History - WebSearch++")
def dashboard() -> rx.Component:
    """The history page.

    Returns:
        The UI for the history page.

    """
    return rx.flex(
    rx.container(
        rx.card("This content is constrained to a max width of 448px.", width="100%"),
        size="1",
    ),
    rx.container(
        rx.card("This content is constrained to a max width of 688px.", width="100%"),
        size="2",
    ),
    rx.container(
        rx.card("This content is constrained to a max width of 880px.", width="100%"),
        size="3",
    ),
    rx.container(
        rx.card("This content is constrained to a max width of 1136px.", width="100%"),
        size="4",
    ),
    background_color="var(--gray-3)",
    spacing="0",
    width="100%",
    direction="column",
    align="end",
)