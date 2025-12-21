import reflex as rx


def Ubicacion() -> rx.Component:
    return rx.box(
        rx.vstack(
            # TÍTULO
            rx.heading(
                "Dónde estamos",
                size="8",
            ),

            rx.text(
                "Restaurante Barrón",
                size="5",
                font_weight="bold",
            ),

            rx.text(
                "Calle Mayor 25, 28013 Madrid",
                size="4",
                color="gray.600",
            ),

            # BOTÓN GOOGLE MAPS
            rx.link(
                rx.button(
                    "Cómo llegar",
                    bg_color="#1a73e8",
                    color="white",
                    padding_x="2rem",
                    border_radius="md",
                    _hover={"bg_color": "#1558b0"},
                ),
                href="https://www.google.com/maps?q=40.416775,-3.703790",
                is_external=True,
            ),

            # MAPA EMBEBIDO
            rx.box(
                rx.html(
                    """
                    <iframe
                        src="https://www.google.com/maps?q=40.416775,-3.703790&z=16&output=embed"
                        width="100%"
                        height="100%"
                        style="border:0;"
                        loading="lazy"
                        referrerpolicy="no-referrer-when-downgrade">
                    </iframe>
                    """
                ),
                width="100%",
                height="400px",
                border_radius="lg",
                overflow="hidden",
                margin_top="2rem",
            ),

            spacing="4",
            align_items="start",
            max_width="1200px",
            margin="0 auto",
            padding="4rem 2rem",
        ),
        width="100%",
        background_color="#c71717",
    )

app = rx.App()
app.add_page(Ubicacion)
