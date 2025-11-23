"""A component to display a single search history entry."""
import reflex as rx
from vue.states.history_state import HistoryState, HistoryEntry


def history_entry_card(entry: HistoryEntry) -> rx.Component:
    """Render a single history entry card."""
    return rx.card(
        rx.flex(
            rx.box(
                rx.flex(
                    rx.icon("globe", size=16, color="gray"),
                    rx.badge(entry.searchEngine, variant="outline"),
                    rx.icon("calendar", size=16, color="gray", margin_left="10px"),
                    rx.moment(
                        unix_timestamp=entry.timestamp,
                        format="DD MMM YYYY, HH:mm",
                        size="2",
                        color_scheme="gray"
                    ),
                    spacing="2",
                    align="center",
                ),
                rx.box(
                    rx.code(entry.query),
                    bg="var(--gray-3)",
                    padding="10px",
                    border_radius="var(--radius-2)",
                    margin_y="10px",
                    width="100%",
                ),
                rx.flex(
                    rx.cond(
                        entry.parameters.contains("fileType"),
                        rx.badge(
                            rx.text("filetype:", entry.parameters["fileType"]),
                            variant="solid",
                            color_scheme="gray"
                        ),
                    ),
                    rx.cond(
                        entry.parameters.contains("site"),
                        rx.badge(
                            rx.text("site:", entry.parameters["site"]),
                            variant="solid",
                            color_scheme="gray"
                        ),
                    ),
                    spacing="2",
                    wrap="wrap",
                ),
                flex="1",
            ),
            rx.flex(
                rx.icon_button(
                    "copy",
                    on_click=lambda: HistoryState.copy_query(entry.query),
                    variant="ghost",
                    title="Copy",
                ),
                rx.icon_button(
                    "search",
                    # on_click=lambda: HistoryState.load_query(entry), # Need to implement this
                    variant="ghost",
                    title="Load this search",
                ),
                rx.icon_button(
                    "trash-2",
                    on_click=lambda: HistoryState.delete_entry(entry.id),
                    variant="ghost",
                    color_scheme="red",
                    title="Delete",
                ),
                spacing="2",
                margin_left="16px",
            ),
            justify="between",
            align="start",
        ),
        width="100%",
    )
