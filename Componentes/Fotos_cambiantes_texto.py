import reflex as rx


def Fotos_cambiantes_texto_derecha() -> rx.Component:
    return rx.box(
        rx.hstack(
            # CONTENEDOR DE IMÁGENES (UNA SOLA ZONA)
            rx.box(
                # IMAGEN 1
                rx.image(
                    src="Naturaleza.jpg",
                    position="absolute",
                    top="0",
                    left="0",
                    width="100%",
                    height="100%",
                    object_fit="cover",
                    animation="fade1 15s infinite",
                ),

                # IMAGEN 2
                rx.image(
                    src="Cascada.jpg",
                    position="absolute",
                    top="0",
                    left="0",
                    width="100%",
                    height="100%",
                    object_fit="cover",
                    animation="fade2 15s infinite",
                ),

                # IMAGEN 3
                rx.image(
                    src="unnamed.jpg",
                    position="absolute",
                    top="0",
                    left="0",
                    width="100%",
                    height="100%",
                    object_fit="cover",
                    animation="fade3 15s infinite",
                ),

                width="50%",
                height="500px",
                position="relative",
                overflow="hidden",
                border_radius="10px",

                # ANIMACIONES CSS
                sx={
                    "@keyframes fade1": {
                        "0%": {"opacity": "1"},
                        "30%": {"opacity": "1"},
                        "33%": {"opacity": "0"},
                        "100%": {"opacity": "0"},
                    },
                    "@keyframes fade2": {
                        "0%": {"opacity": "0"},
                        "33%": {"opacity": "0"},
                        "36%": {"opacity": "1"},
                        "63%": {"opacity": "1"},
                        "66%": {"opacity": "0"},
                        "100%": {"opacity": "0"},
                    },
                    "@keyframes fade3": {
                        "0%": {"opacity": "0"},
                        "66%": {"opacity": "0"},
                        "69%": {"opacity": "1"},
                        "100%": {"opacity": "1"},
                    },
                },
            ),

            # TEXTO
            rx.vstack(
                rx.heading(
                    "Respeto por nuestro planeta",
                    size="8",
                ),

                rx.text(
                    "Trabajamos con producto local y de temporada, reducimos residuos, "
                    "reciclamos y tomamos decisiones responsables para minimizar "
                    "nuestro impacto ambiental.",
                    size="4",
                    color="gray.600",
                ),

                rx.text(
                    "Porque creemos que cuidar del planeta también forma parte "
                    "de lo que servimos en la mesa.",
                    size="4",
                    font_style="italic",
                ),

                spacing="4",
                align_items="start",
                max_width="500px",
            ),

            spacing="8",
            align_items="center",
            justify="center",
            max_width="1200px",
            margin="0 auto",
            padding="6rem 2rem",
        ),
        width="100%",
        background_color="#b9864b",
    )


app = rx.App()
app.add_page(Fotos_cambiantes_texto_derecha)
