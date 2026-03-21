import reflex as rx


def Compromiso_naturaleza_icono() -> rx.Component:
    return rx.box(
        rx.flex(
            # BLOQUE IZQUIERDO: TEXTO (Ocupa el 50%)
            rx.vstack(
                rx.image(
                    src="Icono_reciclaje.webp",
                    width="110px",
                    height="110px",
                    margin_bottom="1rem",
                ),
                rx.heading(
                    "Respeto por nuestro planeta",
                    size="8",
                    text_align="center",
                    color="#4a3a32",
                ),
                rx.text(
                    "Trabajamos con producto local y de temporada, reducimos residuos, "
                    "reciclamos y tomamos decisiones responsables para minimizar "
                    "nuestro impacto ambiental.",
                    size="4",
                    color="white",
                    text_align="center",
                ),
                rx.text(
                    "Porque creemos que cuidar del planeta también forma parte "
                    "de lo que servimos en la mesa.",
                    size="4",
                    font_style="italic",
                    text_align="center",
                    color="white",
                ),
                width=["100%", "100%", "50%"],
                height=["auto", "auto", "500px"], 
                justify_content="center", 
                align_items="center",
                padding=["2rem", "2rem", "4rem"],
                spacing="5",
            ),

            # BLOQUE DERECHO: FOTOS CON ANIMACIÓN (Ocupa el 50%)
            rx.box(
                rx.image(
                    src="Naturaleza.jpg",
                    position="absolute",
                    top="0", left="0", width="100%", height="100%",
                    object_fit="cover",
                    animation="fade1 15s infinite",
                ),
                rx.image(
                    src="Pintxos_barron.webp",
                    position="absolute",
                    top="0", left="0", width="100%", height="100%",
                    object_fit="cover",
                    animation="fade2 15s infinite",
                ),
                rx.image(
                    src="Cascada.jpg",
                    position="absolute",
                    top="0", left="0", width="100%", height="100%",
                    object_fit="cover",
                    animation="fade3 15s infinite",
                ),
                width=["100%", "100%", "50%"],
                height=["300px", "400px", "500px"],
                position="relative",
                overflow="hidden",
                border_radius="10px",
                box_shadow="0px 10px 30px rgba(0,0,0,0.15)",
                sx={
                    "@keyframes fade1": {
                        "0%": {"opacity": "1"}, "30%": {"opacity": "1"},
                        "33%": {"opacity": "0"}, "100%": {"opacity": "0"},
                    },
                    "@keyframes fade2": {
                        "0%": {"opacity": "0"}, "33%": {"opacity": "0"},
                        "36%": {"opacity": "1"}, "63%": {"opacity": "1"},
                        "66%": {"opacity": "0"}, "100%": {"opacity": "0"},
                    },
                    "@keyframes fade3": {
                        "0%": {"opacity": "0"}, "66%": {"opacity": "0"},
                        "69%": {"opacity": "1"}, "100%": {"opacity": "1"},
                    },
                },
            ),

            # CONFIGURACIÓN RESPONSIVE
            flex_direction=["column-reverse", "column-reverse", "row"], # column-reverse para que en móvil la foto siga arriba si prefieres, o "column" para texto arriba
            align_items="center",
            justify="center",
            max_width="1200px",
            margin="0 auto",
            padding=["2rem 1rem", "4rem 2rem", "6rem 2rem"],
            gap=["2rem", "2rem", "4rem"], # Espacio entre texto y fotos
        ),
        width="100%",
        background_color="#b9864b",

    )

app = rx.App()
app.add_page(Compromiso_naturaleza_icono)



              

