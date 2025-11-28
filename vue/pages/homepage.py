"""The dashboard page."""

import reflex as rx
from vue.components.homepage_header import homepage_header



@rx.page("/", title="Home - WebSearch++")
def dashboard() -> rx.Component:
    """The homepage.

    Returns:
        The UI for the homepage.

    """
    return rx.flex(
        homepage_header()
    )