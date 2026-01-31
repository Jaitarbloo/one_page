
import reflex as rx

from Navbar_trasparente import Navbar_trasparente
from Cabezera import Cabezera
from Nuestra_cocina import cuatro_fotos_pequenas_dos_botones 
from Carrusel_foto_grande import Carrusel_grande
from Nuestro_espacio import El_Local 
from Carrusel_foto_pequena import Carrusel_peque
from Nuestro_equipo import EquipoHumano
from Compromiso_ambiental import Compromiso_naturaleza_icono
from Footer import UbicacionFooter
#from Componente_en_proceso import ....



def index():
    
    return rx.vstack(   
                        
                        Navbar_trasparente(),
                        Cabezera(),
                        cuatro_fotos_pequenas_dos_botones(),
                        Carrusel_grande(),
                        El_Local(),
                        Carrusel_peque(),
                        EquipoHumano(),
                        Compromiso_naturaleza_icono(),
                        UbicacionFooter(),
                        


                    )

    



app = rx.App()
app.add_page(index, title="Onepage....mi ricón de trabajo")
