
import reflex as rx

from One_page.Componentes.Foto_sombras import BMW
from One_page.Componentes.Navbar_trasparente import Navbar_trasparente
from Cabezera import Cabezera
from One_page.Componentes.Carrusel_foto_grande import Carrusel_grande
from One_page.Componentes.Carrusel_foto_pequena import Carrusel_peque
from Compromiso import Compromiso
from One_page.Componentes.Footer1 import Ubicacion
from One_page.Componentes.Footer2 import UbicacionFooter
from Producto_servivio import ProductoServicio
from Cabezera1 import CabezeraImpactante
from Componente_prueba import CabezeraHero



def index():
    
    return rx.vstack(   #🔹 ORDEN DE COMPONENTES

                                            #Navbar / Menú

                                            #Transparente sobre el hero

                                            #Con anclas a secciones

                                            #Logo visible

                                            #Hero / Cabezera

                                            #Imagen de fondo impactante

                                            #Título grande, subtítulo

                                            #CTA (reservar mesa, ver carta)

                                            #Iconos sociales opcionales

                                            #Producto / Servicio

                                            #Qué ofreces (cocina, platos destacados)

                                            #Breve descripción y filosofía

                                            #Imágenes de alta calidad

                                            #CTA opcional (ver carta completa)

                                            #Galería / Carrusel grande

                                            #Fotografías del restaurante, platos, ambiente

                                            #Visual, llamativo

                                            #Refuerza la experiencia

                                            #Valores / Compromiso

                                            #Filosofía: sostenibilidad, respeto, reciclaje

                                            #Equipo humano, atención

                                            #Iconos o imágenes pequeñas que refuercen el mensaje

                                            #Galería secundaria / Carrusel pequeño

                                            #Detalles, comida, eventos especiales

                                            #Complementa la sección de producto/servicio

                                            #Ubicación

                                            #Dirección, mapa embebido de Google Maps

                                            #CTA “Cómo llegar”
                                            
                                            #Opcional: contacto rápido

                                              #Footer

                                            #Información de contacto completa

                                            #Redes sociales

                                            #Horario
                                            
                                            #Aviso legal / derechos 
                        
                        Navbar_trasparente(),
                        CabezeraHero(),
                        #Cabezera(),
                        #CabezeraImpactante(),
                        ProductoServicio(),
                        Carrusel_grande(),
                        #BMW(),
                        Compromiso(),
                        Carrusel_peque(),
                        #Ubicacion(),
                        UbicacionFooter(),
                        


                    )

    


app = rx.App()
app.add_page(index)
