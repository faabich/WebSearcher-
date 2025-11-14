"""The dashboard page."""

import reflex as rx

@rx.page("/", title="Home - WebSearch++")
def dashboard() -> rx.Component:
    """The homepage.

    Returns:
        The UI for the homepage.

    """
    return rx.box(
        rx.hstack(
            rx.input(placeholder="Search the Web", type="text", id="search-input"),
            rx.button("Erase", on_click=rx.set_value("search-input", "")),
        )
    )