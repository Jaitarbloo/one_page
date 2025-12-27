
import reflex as rx

from Navbar_trasparente import Navbar_trasparente
from Cabezera import Fondo_fijo
from Nuestra_cocina import tres_fotos_pequenas 
from Carrusel_foto_grande import Carrusel_grande
from Nuestro_espacio import El_Local 
from Carrusel_foto_pequena import Carrusel_peque
from Nuestro_equipo import EquipoHumano
from Compromiso import Compromiso 
from Footer import UbicacionFooter



def index():
    
    return rx.vstack(   
                        
                        Navbar_trasparente(),
                        Fondo_fijo(),
                        tres_fotos_pequenas(),
                        Carrusel_grande(),
                        El_Local(),
                        Carrusel_peque(),
                        EquipoHumano(),
                        Compromiso(),
                        UbicacionFooter(),
                        


                    )

    


app = rx.App()
app.add_page(index)
