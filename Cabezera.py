import reflex as rx


def Cabezera() -> rx.Component:
    return rx.box(

        # CONTENIDO
        rx.hstack(

            # TEXTO IZQUIERDA
            rx.vstack(
                rx.heading(
                    "Bar Restaurante",
                    size="9",
                    #color="#dd9912",
                ),

                rx.text(
                    "Tu punto de encuentro",
                    size="6",
                    #color="#dd9912", 
                    margin_top="1rem",
                ),

              

             rx.link(
                rx.button(
                    "Reservar mesa",
                    size="3", 
                    padding="1.8rem 3.5rem", # Relleno cómodo
                    font_size="1.25rem",
                    bg="#3d2b1f", 
                    color="white",
                    border_radius="full",
                    margin_top="4rem", 
                    cursor="pointer",
                    _hover={"bg": "#2a1d15", "transform": "translateY(-4px)"},
                    transition="all 0.3s ease",
                ),
                href="https://www.jaitarbloo.com",
                text_decoration="none",
            ),

                align_items="start",
                spacing="4",
                max_width="500px",
            ),


           

            # ICONO INSTAGRAM DERECHA
            rx.link(
                rx.image(
                    src="https://cdn-icons-png.flaticon.com/512/174/174855.png",
                    width="70px",
                    height="70px",
                    _hover={
                        "transform": "scale(1.1)",
                        "transition": "transform 0.2s",
                    },
                ),
                href="https://www.jaitarbloo.com",
                is_external=True,
            ),

            justify="between",
            align_items="center",
            max_width="1200px",
            margin="0 auto",
            padding="0 2rem",
            width="100%",
        ),

        # FONDO CON DEGRADADO + PARALLAX
        background_image="""
            linear-gradient(
                to right,
                rgba(40,25,15,0.75) 0%,
                rgba(40,25,15,0.4) 45%,
                rgba(40,25,15,0.15) 65%
            ),
            url('Pared_fondo_Barron.jpg')
        """,
        background_size="cover",
        background_position="center",
        background_attachment="fixed",

        min_height="100vh",
        width="100%",
        display="flex",
        align_items="center",
    )


app = rx.App()
app.add_page(Cabezera)
