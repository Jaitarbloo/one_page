import reflex as rx

def cuatro_fotos_con_boton() -> rx.Component:
    return rx.box(
        rx.vstack(
            # TÍTULO (Tamaño intermedio 8)
            rx.heading(
                "Elige y disfruta",
                size="8", 
                text_align="center",
                color="#4a3a32",
                margin_bottom="2rem",
            ),

            # BLOQUE DE FOTOS (Medidas equilibradas)
            rx.hstack(
                *[
                    rx.image(
                        src=img,
                        width="260px",    # Ni muy pequeño (220) ni muy grande (320)
                        height="450px",   # Proporción estilizada
                        object_fit="cover",
                        border_radius="10px",
                        box_shadow="0px 10px 25px rgba(0,0,0,0.25)",
                        transition="all 0.3s ease",
                        _hover={"transform": "scale(1.04)"},
                    )
                    for img in [
                        "Ensaladas_barron.webp",
                        "Picoteo_barron.webp",
                        "Bocadillos_barron.webp",
                        "Menus_barron.webp"
                    ]
                ],
                spacing="7", # Separación intermedia
                justify="center",
                width="100%",
                wrap="wrap",
            ),

            # BOTÓN DE RESERVA (Tamaño medio-alto)
            rx.link(
                rx.button(
                    "Reservar mesa",
                    size="4", 
                    padding="2.2rem 4.5rem", # Relleno cómodo
                    font_size="1.25rem",
                    bg="#3d2b1f", 
                    color="white",
                    border_radius="full",
                    margin_top="4rem", 
                    cursor="pointer",
                    _hover={"bg": "#2a1d15", "transform": "translateY(-4px)"},
                    transition="all 0.3s ease",
                ),
                href="tel:900100100",
                text_decoration="none",
            ),

            spacing="4",
            max_width="1250px", # Ancho de contenedor intermedio
            margin="0 auto",
            padding="5.5rem 2rem", # Padding vertical moderado
            align_items="center",
        ),
        width="100%",
        background_color="#d38832",
    )

app = rx.App()
app.add_page(cuatro_fotos_con_boton, route="/")
