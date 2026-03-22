
import reflex as rx

from Navbar_trasparente import Navbar_trasparente_desplegable
from Cabezera import Cabezera
from Nuestra_cocina import cuatro_fotos_con_boton 
from Nuestro_espacio import El_Local 
from Carrusel_foto_pequena import Carrusel_peque
from Nuestro_equipo import EquipoHumano
from Compromiso_ambiental import Compromiso_naturaleza_icono
from Footer import UbicacionFooter


def index():
    
    return rx.vstack(   
                        
                        Navbar_trasparente_desplegable(),
                        
                        Cabezera(),

                        rx.box(Carrusel_peque(),
                            id="Nuestra_cocina",
                            width="100%",
                            scroll_margin_top="120px"
                          ),

                        rx.box(cuatro_fotos_con_boton(),
                            id="Elige_y_Disfruta",
                            width="100%",
                          ),
                                                
                        rx.box(El_Local(),
                            id="Nuestro_espacio",
                            width="100%",
                          ),

                        rx.box(EquipoHumano(),
                            id="Equipo_humano",
                            width="100%",
                          ),

                        rx.box(Compromiso_naturaleza_icono(),
                            id="Sostenibilidad",
                            width="100%",
                          ),

                        rx.box(UbicacionFooter(),
                            id="Reservar",
                            width="100%",
                          ),

                        spacing="0",
                        align="center",                     
                        


                    )

    



app = rx.App(html_lang="es")
app.add_page(index, title="Ejemplo Onepage")
