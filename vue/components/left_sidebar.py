import reflex as rx

def left_sidebar() -> rx.Component:
    """
    Creates the left sidebar with the history button.
    """
    return rx.vstack(
        rx.button(
            rx.icon(tag="history", size=18),
            " Voir historique",
            variant="outline",
            color_scheme="gray",
            cursor="pointer",
        ),
        spacing="4",
        align="start",
        padding="4",
        border_right="1px solid",
        border_color=rx.color("gray", 4),
        height="100vh", # make the sidebar stretch full height
    )