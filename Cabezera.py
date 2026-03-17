import reflex as rx


def Cabezera() -> rx.Component:
    return rx.box(

        # CONTENIDO
        rx.hstack(

            # TEXTO IZQUIERDA
            rx.vstack(
                rx.heading(
                    "Taberna BARRÓN",
                    size="9",
                    color="#dd9912",
                ),

                rx.text(
                    "Tu punto de encuentro",
                    size="6",
                    color="#dd9912",
                    margin_top="1rem",
                ),

                rx.button(
                    "RESERVAR MESA",
                    bg="#3d2b1f",
                    color="#e7e5ce",
                    padding_x="1.5rem",
                    padding_y="1.2rem",
                    border_radius="md",
                    margin_top="2rem",
                    _hover={"bg_color": "#3b2f2a"},
                ),

                align_items="start",
                spacing="4",
                max_width="500px",
            ),

            # ICONO INSTAGRAM DERECHA
            rx.link(
                rx.image(
                    src="https://cdn-icons-png.flaticon.com/512/174/174855.png",
                    width="70px",
                    height="70px",
                    _hover={
                        "transform": "scale(1.1)",
                        "transition": "transform 0.2s",
                    },
                ),
                href="https://www.instagram.com/bar_barron/",
                is_external=True,
            ),

            justify="between",
            align_items="center",
            max_width="1200px",
            margin="0 auto",
            padding="0 2rem",
            width="100%",
        ),

        # FONDO CON DEGRADADO + PARALLAX
        background_image="""
            linear-gradient(
                to right,
                rgba(40,25,15,0.75) 0%,
                rgba(40,25,15,0.4) 45%,
                rgba(40,25,15,0.15) 65%
            ),
            url('Pared_fondo_Barron.jpg')
        """,
        background_size="cover",
        background_position="center",
        background_attachment="fixed",

        min_height="100vh",
        width="100%",
        display="flex",
        align_items="center",
    )


app = rx.App()
app.add_page(Cabezera)
