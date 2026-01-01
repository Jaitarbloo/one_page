import reflex as rx

config = rx.Config(
    app_name="One_page",
    api_url="https://one-zrwg.onrender.com:8000",
    cors_allowed_origins=[
        "http://localhost:3000",
        "http://https://one-page-exqm.vercel.app/",
        "https://www.jaitarbloo.es/"
        ],
    
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)