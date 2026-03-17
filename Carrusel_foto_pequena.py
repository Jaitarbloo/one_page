import reflex as rx

def Carrusel_peque() -> rx.Component:
    # Simplificamos la lista dejando solo las rutas de las imágenes
    slides = [
        "Desayuno_Barron.png",
        "Ensalada_Barron.jpg",
        "Hamburguesa_Barron.jpg",
        "unnamed.jpg ",
        #"unnamed.jpg",
    ]

    return rx.box(
        rx.hstack(
            *[
                rx.box(
                    rx.image(
                        src=image,
                        # Aumentamos el tamaño (Móvil, Tablet, Escritorio)
                        width=["250px", "350px", "450px"], 
                        height=["180px", "250px", "320px"],
                        object_fit="cover",
                        border_radius="10px", # Bordes un poco más redondeados para el nuevo tamaño
                        transition="transform 0.4s ease",
                        _hover={"transform": "scale(1.05)"},
                    ),
                    position="relative",
                    flex="0 0 auto",
                )
                # Multiplicamos la lista para el efecto infinito
                for image in slides * 2
            ],
            gap=["1.5rem", "2rem", "3rem"],
            animation="carousel-move 40s linear infinite", # Un poco más lento por ser fotos más grandes
            _hover={"animation_play_state": "paused"},
        ),
        width="100%",
        overflow="hidden",
        padding_y=["3rem", "4rem", "5rem"],
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
