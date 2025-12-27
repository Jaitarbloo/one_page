import reflex as rx


def Fondo_fijo() -> rx.Component:
    return rx.box(
        rx.hstack(
            # BLOQUE TEXTO
            rx.vstack(
                rx.heading(
                    "BAR BARRÓN",
                    size="9",
                    color="white",
                    text_shadow="2px 4px 12px rgba(0,0,0,0.7)",
                    sx={"animation": "slideFade 1.2s ease forwards"}
                ),
                rx.text(
                    "Cocina honesta. Personas primero.",
                    size="6",
                    color="white",
                    margin_top="1rem",
                    text_shadow="1px 2px 8px rgba(0,0,0,0.6)",
                    sx={"animation": "slideFade 1.2s ease forwards", "animation_delay": "0.3s"}
                ),
                rx.text(
                    "Producto local · Respeto · Sostenibilidad",
                    size="4",
                    color="#e6dccf",
                    margin_top="0.5rem",
                    sx={"animation": "slideFade 1.2s ease forwards", "animation_delay": "0.6s"}
                ),
                rx.button(
                    "Reservar mesa",
                    bg_color="#e6dccf",
                    color="#4a3a32",
                    border_radius="lg",
                    padding_x="2.5rem",
                    padding_y="1.1rem",
                    font_size="5",
                    margin_top="2.5rem",
                    sx={
                        "animation": "slideFade 1.2s ease forwards",
                        "animation_delay": "0.9s",
                        "opacity": "0"
                    },
                    _hover={
                        "bg_color": "#d2b48c",
                        "transform": "scale(1.05)",
                        "transition": "all 0.3s"
                    }
                ),
                align_items="start",
                justify="center",
                padding_left="10rem",
                max_width="700px"
            ),

            # BLOQUE ICONOS
            rx.vstack(
                rx.link(
                    rx.image(
                        src="https://cdn-icons-png.flaticon.com/512/174/174855.png",
                        width="60px",
                        height="60px",
                        opacity="0.85",
                        _hover={"transform": "scale(1.15)", "transition": "0.3s"}
                    ),
                    href="https://www.instagram.com/bar_barron/",
                    is_external=True
                ),
                align_items="center",
                justify="center",
                width="15%"
            ),

            width="100%",
            justify="between",
            align_items="center",
            min_height="100vh"
        ),

        # FONDO + PARALLAX
        background_image="""
            linear-gradient(
                to right,
                rgba(40,25,15,0.75) 0%,
                rgba(40,25,15,0.4) 45%,
                rgba(40,25,15,0.15) 65%
            ),
            url('/Pared_fondo_Barron.jpg')
        """,
        background_size="cover",
        background_position="center",
        background_attachment="fixed",
        width="100%",
        min_height="100vh",
        position="relative",

        # ANIMACIONES
        sx={
            "@keyframes slideFade": {
                "0%": {"opacity": "0", "transform": "translateY(30px)"},
                "100%": {"opacity": "1", "transform": "translateY(0)"}
            }
        }
    )


app = rx.App()
app.add_page(Fondo_fijo)
