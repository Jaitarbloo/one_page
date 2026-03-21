import reflex as rx

def Navbar_trasparente_desplegable() -> rx.Component:
    menu_items = [
        ("Nuestra cocina", "#Nuestra_cocina"),
        ("Elige y disfruta", "#Elige_y_Disfruta"),
        ("Nuestro espacio", "#Nuestro_espacio"),
        ("Equipo humano", "#Equipo_humano"),
        ("Sostenibilidad", "#Sostenibilidad"),
        ("Reservar", "#Reservar"),
    ]

    return rx.center( # Centra todo el bloque en la pantalla
        rx.vstack(
            # --- FILA DE CONTENIDO ---
            rx.hstack(
                # FOTO
                rx.image(
                    src="/Copa_barron.jpg",
                    height=rx.breakpoints(initial="35px", lg="45px"),
                    width="auto",
                ),

                # MENÚ ESCRITORIO
                rx.hstack(
                    *[
                        rx.link(
                            rx.text(text, size="5", color="white", _hover={"opacity": 0.7}),
                            href=url
                        ) for text, url in menu_items
                    ],
                    spacing="8",
                    display=rx.breakpoints(initial="none", lg="flex"),
                    margin_left="3em", 
                ),

                # MENÚ MÓVIL
                rx.box(
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.button(
                                rx.icon("menu", color="white", size=30),
                                variant="ghost",
                                cursor="pointer",
                            )
                        ),
                        rx.menu.content(
                            *[
                                rx.menu.item(text, on_click=rx.redirect(url)) 
                                for text, url in menu_items
                            ],
                            background_color="rgba(0, 0, 51, 0.9)",
                        ),
                    ),
                    display=rx.breakpoints(initial="block", lg="none"),
                ),
                
                # Separación extrema en móvil, juntos en PC
                justify=rx.breakpoints(initial="between", lg="center"),
                align="center",
                width="100%",
            ),

            # --- LÍNEA BLANCA (Ajustada al contenido) ---
            rx.box(
                height="1px",
                bg="white",
                width="100%",
                margin_top="0.5em",
            ),
            
            spacing="0",
            # En móvil forzamos un ancho casi total para que se vean los extremos.
            # En PC dejamos que mida lo que midan los textos (fit-content).
            width=rx.breakpoints(initial="90vw", lg="fit-content"),
            align="center",
        ),
        background="transparent",
        position="fixed",
        top="0",
        z_index="999",
        width="100%",
        padding_top="1.5em",
    )
