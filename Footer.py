import reflex as rx

def UbicacionFooter() -> rx.Component:
    # URL directa para el botón "Cómo llegar"
    maps_url = "https://www.google.com/maps/place/Madrid/@40.4380986,-3.8443497,11z/data=!3m1!4b1!4m6!3m5!1s0xd422997800a3c81:0xc436dec1618c2269!8m2!3d40.4167279!4d-3.7032905!16zL20vMDU2X3k?entry=ttu&g_ep=EgoyMDI2MDMxOC4xIKXMDSoASAFQAw%3D%3D"
    
    return rx.box(
        rx.vstack(
            # Columna de Texto Centrada
            rx.vstack(
                rx.heading(
                    "Dónde estamos",
                    size="8",
                    color="#f5f3ef",
                    margin_bottom="1rem",
                ),
                rx.text(
                    "Bar Restaurante",
                    size="6",
                    font_weight="bold",
                    color="#f5f3ef",
                ),
                rx.text(
                    "Vendita Polinesia,2",
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
                align_items="center",  # Centra el contenido internamente
                text_align="center",    # Centra las líneas de texto
                width="100%",           # Ocupa todo el ancho disponible
            ),

            rx.divider(border_color="rgba(245,243,239,0.2)", margin_y="3rem"),

            # PIE DE PÁGINA
            rx.flex(
                rx.text("© 2025 Bar Restaurante ", size="3", color="#d8d2c8"),
                rx.hstack(
                    rx.link("jaitardev@gmail.com", href="#", color="#d8d2c8", size="3"),
                    #rx.link("Privacidad", href="#", color="#d8d2c8", size="3"),
                    spacing="5",
                ),
                justify="between",
                width="100%",
                flex_direction=["column", "row"],
                align_items="center",
                gap="1rem",
            ),

            max_width="800px", # Reducido un poco para que el texto no se vea muy disperso
            margin="0 auto",
            padding=["3rem 1rem", "5rem 2rem"],
            align_items="center", # Asegura que todo el vstack esté centrado
            
        ),
        width="100%",
        background_color="#4a3a32",
        
    )

app = rx.App()
app.add_page(UbicacionFooter)
