import reflex as rx

config = rx.Config(
    app_name="One_page",
    api_url="https://one-zrwg.onrender.com:8000",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)