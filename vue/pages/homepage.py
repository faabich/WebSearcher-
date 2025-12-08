import reflex as rx
from vue.components.homepage_header import homepage_header
from vue.components.previous_page_button import previous_page_button
from vue.components.quick_help_card import quick_help_card
from vue.components.special_operators_card import special_operators_card
from vue.components.query_card import query_card
#from vue.components.search_term_section import search_term_section

def placeholder_card(text):
    # Emulate an imported card components
    return rx.card(
        rx.text(text, color="white", font_weight="bold"),
        width="100%",
        bg="#222",
    )

@rx.page("/", title="Card Layout Template")
def dashboard() -> rx.Component:
    return rx.flex(
        # 1. Header
        rx.flex(
            rx.hstack(
                homepage_header(),
                # previous_page_button(on_click_handler="HistoryState.go_back"),
                spacing="5",
            ),
            width="100%", padding="2em", justify="center"
        ),

        # 2. Body container
        rx.flex(
            
            # Left column component stack
            rx.vstack(
                placeholder_card("Component 1 (Search Engine Card)"),
                #search_term_section(),
                special_operators_card(),
                placeholder_card("Component 4 (Additional Filter Card)"),
                # Layout properties for Left Panel
                width=["100%", "100%", "100%", "65%"], 
                spacing="5",
            ),
            # Right column component stack
            rx.vstack(
                query_card(),
                quick_help_card(),
                width=["100%", "100%", "100%", "30%"], 
                spacing="5",
            ),

            # flex styling
            width="100%",
            spacing="5",
            flex_direction=["column", "column", "column", "row"], # Responsive flex direction (stack components vertically on mobile, horizontally on desktop)
            justify="center", # Reflex shorthand for CSS justify-content: center
            align="start",
            padding="2em",
        ),

        # header - body layout properties
        direction="column",
        width="100%",
        min_height="100vh",
        bg="#111",
    )