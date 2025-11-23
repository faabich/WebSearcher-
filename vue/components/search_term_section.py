import reflex as rx

def search_term_section() -> rx.Component:
    """
    Section for "Terme de recherche".
    """
    return rx.card(
        rx.vstack(
            rx.heading("Terme de recherche", size="5"), # FIX 1: size="5"
            rx.form.field(
                rx.form.control(
                    rx.input(placeholder="Terme 1..."),
                ),
                name="term1",
                width="100%",
            ),
            rx.button(
                rx.icon(tag="plus", size=18),
                " Ajouter un terme",
                width="100%",
                cursor="pointer",
                variant="outline",
            ),
            spacing="3",
            align="stretch",
        ),
        width="100%",
    )