import reflex as rx

config = rx.Config(
    app_name="One_page",
    admin_dash=False,
    api_url="https://one-zrwg.onrender.com:8000",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)