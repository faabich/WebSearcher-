"""A component to display a single special operators card."""
import reflex as rx
from vue.states.home_state import HomeState


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
                        value=HomeState.OS_def,
                        on_change=lambda value: HomeState.set_OS_values(1, value),
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
                        value=HomeState.OS_weather,
                        on_change=lambda value: HomeState.set_OS_values(2, value),
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
                        value=HomeState.OS_action,
                        on_change=lambda value: HomeState.set_OS_values(2, value),
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
                        value=HomeState.OS_map,
                        on_change=lambda value: HomeState.set_OS_values(2, value),
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
                        value=HomeState.OS_movie,
                        on_change=lambda value: HomeState.set_OS_values(2, value),
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
