import reflex as rx

def Cabezera() -> rx.Component:
    
    return rx.box(# Contenedor con imagen de fondo 
        
                    rx.flex(# Columna izquierda con textos y botones
                                
                                rx.vstack(
                                            rx.heading("BAR   BARRON",
                                                        size="8",
                                                        color="brown",
                                                        ),
                
                                            rx.text("Tu punto de encuentro",
                                                    size="7",
                                                    color="brown",
                                                    margin_top="1rem"
                                                    ),
                
               
                                    align_items="start",
                                    justify="center",
                                    padding_x="15rem",
                                    width="80%"
                                        
                                            ),

                                # Icono Instagram a la derecha
                                rx.vstack(
                                            
                                            rx.link(
                                                    
                                                    rx.image(src="https://cdn-icons-png.flaticon.com/512/174/174855.png",
                                                            width="100px",
                                                            height="100px",
                                                            _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"}
                                                            ),
                    
                                                href="https://www.instagram.com/bar_barron/",
                                                is_external=True
                                                    
                                                    ),
                
                                    width="20%",
                                   
                                        ),

                        align_items="center",
                        width="100%",
                        min_height="80vh"
                            
                            ),
        
        # Imagen de fondo + overlay negro degradado
        background_image="url('/Pared_fondo_Barron.jpg')",
        background_size="cover",
        background_position="center",
        min_height="100vh",
        width="100%"
                
                )




app = rx.App()
app.add_page(Cabezera)

