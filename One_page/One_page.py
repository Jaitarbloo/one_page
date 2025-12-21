
import reflex as rx

from BMW_Publicidad import BMW
from Navbar_trasparente import Navbar_trasparente
from Cabezera import Cabezera
from Carrusel_foto_grande import Carrusel_grande
from Carrusel_foto_pequena import Carrusel_peque
from Compromiso import Compromiso
from Ubicacion import Ubicacion
#from Componente_prueba1 import Ubicacion
#from Componente_prueba import Compromiso



def index():
    
    return rx.vstack(

                        Navbar_trasparente(),
                        Cabezera(),
                        BMW(),
                        Compromiso(),
                        Carrusel_grande(),
                        Carrusel_peque(),
                        Ubicacion(),
                        


                    )

    


app = rx.App()
app.add_page(index)
