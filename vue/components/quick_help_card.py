"""A component to display a single quick help card."""
import reflex as rx



def quick_help_card() -> rx.Component:
    """Render a single quick help card."""
    return rx.flex(
        rx.card(
            rx.flex(
                rx.text("Aide rapide", size="3"),
                rx.spacer(),
                rx.text(rx.text.strong("AND")," - Tous les mots"),
                rx.text(rx.text.strong("OR"), " - Au moins un mot"),
                rx.text(rx.text.strong('""'), " - Expression exacte"),
                rx.text(rx.text.strong("+"), " - Exclure un mot"),
                rx.text(rx.text.strong("-"), " - Inclure un mot"),
                rx.divider(),
                rx.text(rx.text.strong("site:"), " - Limiter à un site"),
                rx.text(rx.text.strong("filetype:"), " - Type de fichier"),
                rx.text(rx.text.strong("intitle:"), " - Dans le titre"),
                rx.text(rx.text.strong("inurl:"), " - Dans l'URL"),
                rx.text(rx.text.strong("intext:"), " - Dans le texte"),
                rx.text(rx.text.strong("related:"), " - Lié à"),
                rx.text(rx.text.strong("location:"), " - Lieu"),
                rx.text(rx.text.strong("around:"), " - Autour de"),
                rx.text(rx.text.strong("grouped:"), " - Termes groupés"),
                rx.text(rx.text.strong("define:"), " - Définir"),
                rx.text(rx.text.strong("weather:"), " - Météo"),
                rx.text(rx.text.strong("stocks:"), " - Actions"),
                rx.text(rx.text.strong("map:"), " - Carte"),
                rx.text(rx.text.strong("movie:"), " - Film"),
                rx.text(rx.text.strong("source:"), " - Source"),
                rx.text(rx.text.strong("near:"), " - Proche de"),

                direction="column",
                spacing="2"
            ),
            width="100%"
        ),
        width="100%"
    )