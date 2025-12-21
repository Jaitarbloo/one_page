import reflex as rx

config = rx.Config(
    app_name="One_page",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)