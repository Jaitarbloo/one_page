import reflex as rx

config = rx.Config(
    app_name="One_page",
    api_url="https://one-zrwg.onrender.com",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://one-page-exqm.vercel.app",
        "https://www.jaitarbloo.es"
        ],
    
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)