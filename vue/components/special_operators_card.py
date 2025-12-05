"""A component to display a single special operators card."""
import reflex as rx
# from vue.states.home_state import HomeState


def special_operators_card() -> rx.Component:
    """Render a single special operators card."""
    return rx.card(
        rx.flex(
            rx.box(
                rx.heading("Opérateurs spéciaux", size="3")
            )
        ),
        rx.flex(
            rx.box(
                rx.flex(
                    rx.text("Définition (define:)", size="1"),
                    spacing="2",
                    align="center",
                ),
                rx.flex(
                    rx.input(
                        placeholder="Mot à définir"
                    )
                )
            ),
            rx.box(
                rx.flex(
                    rx.text("Météo (weather:)", size="1"),
                    spacing="2",
                    align="center",
                ),
                rx.flex(
                    rx.input(
                        placeholder="Lieu"
                    )
                )
            ),
            rx.box(
                rx.flex(
                    rx.text("Actions (stocks:)", size="1"),
                    spacing="2",
                    align="center",
                ),
                rx.flex(
                    rx.input(
                        placeholder="Symbole (ex: AAPL)"
                    )
                )
            ),
            rx.box(
                rx.flex(
                    rx.text("Carte (map:)", size="1"),
                    spacing="2",
                    align="center",
                ),
                rx.flex(
                    rx.input(
                        placeholder="Lieu"
                    )
                )
            ),
            rx.box(
                rx.flex(
                    rx.text("Film (movie:)", size="1"),
                    spacing="2",
                    align="center",
                ),
                rx.flex(
                    rx.input(
                        placeholder="Titre du Film"
                    )
                )
            ),
            spacing="2",
            width="100",
            flex_wrap="wrap"
        ),
        width="100%",
    )
