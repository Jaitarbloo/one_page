
import reflex as rx

from Navbar_trasparente import Navbar_trasparente_desplegable
from Cabezera import Cabezera
from Nuestra_cocina import cuatro_fotos_con_boton 
from Carrusel_foto_grande import Carrusel_grande
from Nuestro_espacio import El_Local 
from Carrusel_foto_pequena import Carrusel_peque
from Nuestro_equipo import EquipoHumano
from Compromiso_ambiental import Compromiso_naturaleza_icono
from Footer import UbicacionFooter
#from Componente_en_proceso import ....


def index():
    
    return rx.vstack(   
                        
                        Navbar_trasparente_desplegable(),
                        Cabezera(),
                        Carrusel_peque(),
                        cuatro_fotos_con_boton(),
                        #Carrusel_grande(),
                        El_Local(),
                        EquipoHumano(),
                        Compromiso_naturaleza_icono(),
                        UbicacionFooter(),

                        spacing="0"
                        


                    )

    



app = rx.App(html_lang="es")
app.add_page(index, title="Onepage....mi ricón de trabajo")
