import reflex as rx


def Foto_mediana_con_texto() -> rx.Component:
    return rx.box(
        rx.hstack(
            # IMAGEN
            rx.image(
                src="Terraza_Barron.jpg",  # tu imagen
                width="50%",
                height="500px",
                border_radius="10px",
            ),

            # TEXTO
            rx.vstack(
                rx.heading(
                    "Personas y planeta",
                    size="8",
                ),

                rx.text(
                    "Creemos que la buena cocina empieza por el respeto.",
                    size="5",
                    font_weight="bold",
                ),

                rx.text(
                    "Cuidamos de nuestro equipo, fomentando un entorno de trabajo "
                    "justo, humano y colaborativo.",
                    size="4",
                    color="gray.600",
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
app.add_page(Foto_mediana_con_texto)