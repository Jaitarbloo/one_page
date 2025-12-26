
import reflex as rx

from Foto_sombras import BMW
from Navbar_trasparente import Navbar_trasparente
from Cabezera import Cabezera
from Carrusel_foto_grande import Carrusel_grande
from Carrusel_foto_pequena import Carrusel_peque
from Compromiso import Compromiso
from Footer1 import Ubicacion
from Footer2 import UbicacionFooter
from Producto_servivio import ProductoServicio



def index():
    
    return rx.vstack(

                        Navbar_trasparente(),
                        Cabezera(),
                        ProductoServicio(),
                        Carrusel_grande(),
                        #BMW(),
                        Compromiso(),
                        Carrusel_peque(),
                        Ubicacion(),
                        UbicacionFooter(),
                        


                    )

    


app = rx.App()
app.add_page(index)
