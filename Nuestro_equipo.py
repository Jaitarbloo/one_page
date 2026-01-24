import reflex as rx


def EquipoHumano() -> rx.Component:
    return rx.flex(
        rx.hstack(
            # IMAGEN
            rx.box(
                background_image="url('/Camareros.jpg')",
                background_size="cover",
                background_position="center",
                width="50%",
                min_height="500px",
                border_radius="xl",
            ),

            # TEXTO
            rx.vstack(
                rx.heading(
                    "Nuestro equipo marca la diferencia",
                    size="7",
                    color="#4a3a32",
                ),

                rx.text(
                    "En Bar Barrón creemos que un buen servicio empieza "
                    "mucho antes de servir una mesa.",
                    size="4",
                    color="gray.700",
                ),

                rx.text(
                    "Seleccionamos a nuestro equipo por su actitud, "
                    "capacidad de escucha y respeto por las personas. "
                    "Buscamos camareros que disfruten atendiendo, "
                    "que entiendan el ritmo del bar y que traten a cada cliente "
                    "como le gustaría ser tratado.",
                    size="4",
                    color="gray.700",
                ),

                rx.text(
                    "La formación continua, el trabajo en equipo y "
                    "unas condiciones laborales justas son la base "
                    "para ofrecer un trato cercano, profesional y humano.",
                    size="4",
                    color="gray.700",
                ),

                rx.hstack(
                    rx.text("✔ Actitud y cercanía", size="4", color="#4a3a32"),
                    rx.text("✔ Formación continua", size="4", color="#4a3a32"),
                    rx.text("✔ Respeto y compromiso", size="4", color="#4a3a32"),
                    spacing="4",
                ),

                spacing="4",
                align_items="start",
            ),

            spacing="6",
            align_items="center",
            max_width="1200px",
            margin="0 auto",
            padding="6rem 2rem",
        ),

        width="100%",
        background_color="#0e0c0a",
    )

app = rx.App()
app.add_page(EquipoHumano)