import reflex as rx

def UbicacionFooter1() -> rx.Component:
    # URL directa para el botón "Cómo llegar" a la calle Pintorería 2, Vitoria
    maps_url = "https://www.google.com"
    
    return rx.box(
        rx.vstack(
            rx.flex(
                # Columna de Texto
                rx.vstack(
                    rx.heading(
                        "Dónde estamos",
                        size="8",
                        color="#f5f3ef",
                        margin_bottom="1rem",
                    ),
                    rx.text(
                        "Taberna Barrón",
                        size="6",
                        font_weight="bold",
                        color="#f5f3ef",
                    ),
                    rx.text(
                        "Pintore Kalea, 2, 01001 Vitoria-Gasteiz, Araba",
                        size="4",
                        color="#d8d2c8",
                    ),
                    rx.text(
                        "Tel. 945 13 13 41",
                        size="4",
                        color="#d8d2c8",
                    ),
                    rx.text(
                        "Horario: Lunes a Domingo · 11:00 – 00:00",
                        size="4",
                        color="#d8d2c8",
                    ),
                    rx.link(
                        rx.button(
                            "Cómo llegar",
                            bg="#e6dccf",
                            color="#4a3a32",
                            padding_x="2rem",
                            border_radius="md",
                            margin_top="1.5rem",
                            _hover={"bg": "#d2b48c"},
                        ),
                        href=maps_url,
                        is_external=True,
                    ),
                    spacing="2",
                    align_items="start",
                    width=["100%", "100%", "40%"],
                ),

                # BLOQUE DEL MAPA (Corregido para que se vea)
                rx.box(
                    rx.html(
                        """
                        <iframe 
                            width="100%" 
                            height="400" 
                            frameborder="0" 
                            scrolling="no" 
                            marginheight="0" 
                            marginwidth="0" 
                            src="https://maps.google.com">
                        </iframe>
                        """
                    ),
                    width=["100%", "100%", "60%"],
                    border_radius="15px",
                    overflow="hidden",
                    box_shadow="lg",
                ),

                flex_direction=["column", "column", "row"],
                spacing="8",
                width="100%",
                align_items="center",
            ),

            rx.divider(border_color="rgba(245,243,239,0.2)", margin_y="3rem"),

            # PIE DE PÁGINA
            rx.flex(
                rx.text("© 2025 Taberna Barrón - Vitoria-Gasteiz", size="3", color="#d8d2c8"),
                rx.hstack(
                    rx.link("Aviso legal", href="#", color="#d8d2c8", size="3"),
                    rx.link("Privacidad", href="#", color="#d8d2c8", size="3"),
                    spacing="4",
                ),
                justify="between",
                width="100%",
                flex_direction=["column", "row"],
                align_items="center",
                gap="1rem",
            ),

            max_width="1200px",
            margin="0 auto",
            padding=["3rem 1rem", "5rem 2rem"],
        ),
        width="100%",
        background_color="#4a3a32",
    )

app = rx.App()
app.add_page(UbicacionFooter1)
