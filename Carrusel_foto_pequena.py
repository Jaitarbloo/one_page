import reflex as rx

def Carrusel_peque() -> rx.Component:
    slides = [
        "Bocata_barron.webp",
        "Ensalada_calamares_barron.webp ",
        "Hamburguesa_queso_barron.webp ",
        "Nachos_barron.webp ",
        "Revuelto_tomate_barron.webp",
        "Verduras_barron.webp"
    ]

    return rx.box(
        rx.hstack(
            *[
                rx.box(
                    rx.image(
                        src=image,
                        # Tamaño INTERMEDIO (Móvil, Tablet, Escritorio)
                        width=["210px", "210px", "210px"], 
                        height=["230px", "230px", "230px"],
                        object_fit="cover",
                        border_radius="10px",
                        transition="transform 0.4s ease",
                        _hover={"transform": "scale(1.05)"},
                    ),
                    position="relative",
                    flex="0 0 auto",
                )
                for image in slides * 2
            ],
            gap=["1.2rem", "1.8rem", "2.5rem"],
            # Velocidad intermedia: 25 segundos
            animation="carousel-move 7s linear infinite", 
            _hover={"animation_play_state": "paused"},
        ),
        width="100%",
        overflow="hidden",
        padding_y=["2rem", "3rem", "3.5rem"], # Espaciado vertical equilibrado
        background_color="#b9864b",
        sx={
            "@keyframes carousel-move": {
                "from": {"transform": "translateX(0%)"},
                "to": {"transform": "translateX(-50%)"},
            }
        },
    )

app = rx.App()
app.add_page(Carrusel_peque)
