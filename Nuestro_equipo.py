import reflex as rx

def EquipoHumano() -> rx.Component:
    return rx.flex(
        rx.flex(
            # IMAGEN
            rx.box(
                background_image="url('/Camareros.jpg')",
                background_size="cover",
                background_position="center",
                # 100% en móvil, 50% en escritorio
                width=["100%", "100%", "50%"], 
                min_height=["300px", "400px", "500px"],
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
                    "En Bar Barrón creemos que un buen servicio empieza mucho antes de servir una mesa.",
                    size="4",
                    color="gray.700",
                ),
                rx.text(
                    "Seleccionamos a nuestro equipo por su actitud, capacidad de escucha y respeto por las personas.",
                    size="4",
                    color="gray.700",
                ),
                rx.text(
                    "La formación continua, el trabajo en equipo y unas condiciones laborales justas son la base para ofrecer un trato cercano, profesional y humano.",
                    size="4",
                    color="gray.700",
                ),
                # Lista de checks adaptable
                rx.flex(
                    rx.text("✔ Actitud y cercanía", size="3", color="#4a3a32"),
                    rx.text("✔ Formación continua", size="3", color="#4a3a32"),
                    rx.text("✔ Respeto y compromiso", size="3", color="#4a3a32"),
                    spacing="4",
                    flex_direction=["column", "row", "row"], # Columna en móvil
                ),
                spacing="4",
                align_items="start",
                width=["100%", "100%", "50%"], # 100% en móvil
            ),

            # CONFIGURACIÓN DEL CONTENEDOR FLEX
            # 'column' para móvil (foto arriba, texto abajo)
            # 'row' para escritorio (foto lado a lado)
            flex_direction=["column", "column", "row"],
            spacing="6",
            align_items="center",
            max_width="1200px",
            margin="0 auto",
            padding=["2rem 1rem", "4rem 2rem", "6rem 2rem"], # Menos padding en móvil
        ),
        width="100%",
        background_color="#0e0c0a"
    )

app = rx.App()
app.add_page(EquipoHumano)
