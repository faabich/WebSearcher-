import reflex as rx

config = rx.Config(
    app_name="WebSearcher_",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)