import reflex as rx

def CabezeraImpactante() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Columna izquierda: Textos y CTA
            rx.vstack(
                rx.heading(
                    "BAR BARRÓN",
                    size="9",
                    color="white",
                    text_align="left",
                    text_shadow="2px 2px 8px rgba(0,0,0,0.6)"
                ),
                rx.text(
                    "Tu punto de encuentro",
                    size="6",
                    color="white",
                    margin_top="1rem",
                    text_shadow="1px 1px 6px rgba(0,0,0,0.6)"
                ),
                # Botón CTA
                rx.button(
                    "Reservar ahora",
                    bg_color="#e6dccf",
                    color="#2f0664",
                    border_radius="lg",
                    padding_x="2.5rem",
                    padding_y="1rem",
                    font_size="5",
                    margin_top="2rem",
                    _hover={"bg_color": "#d2b48c", "transform": "scale(1.05)", "transition": "all 0.3s"}
                ),
                spacing="3",
                align_items="start",
                justify="center",
                padding_x="10rem",
                # Animación de aparición suave
                sx={
                    "animation": "fadeIn 1.5s ease-in-out"
                }
            ),

            # Columna derecha: Icono Instagram
            rx.vstack(
                rx.link(
                    rx.image(
                        src="https://cdn-icons-png.flaticon.com/512/174/174855.png",
                        width="70px",
                        height="70px",
                        _hover={"transform": "scale(1.2)", "transition": "transform 0.3s"}
                    ),
                    href="https://www.instagram.com/bar_barron/",
                    is_external=True
                ),
                align_items="center",
                justify="center",
                width="20%"
            ),

            width="100%",
            align_items="center",
            justify="between",  # CORREGIDO: 'between' en lugar de 'space-between'
            min_height="90vh"
        ),
        # Imagen de fondo + overlay degradado
        background_image="""
            linear-gradient(
                to right,
                rgba(0,0,0,0.6) 0%,
                rgba(0,0,0,0.2) 40%,
                rgba(0,0,0,0) 60%
            ),
            url('/Pared_fondo_Barron.jpg')
        """,
        background_size="cover",
        background_position="center",
        width="100%",
        min_height="100vh",
        position="relative",
        sx={
            "@keyframes fadeIn": {
                "0%": {"opacity": "0", "transform": "translateY(20px)"},
                "100%": {"opacity": "1", "transform": "translateY(0)"},
            }
        }
    )

app = rx.App()
app.add_page(CabezeraImpactante)
