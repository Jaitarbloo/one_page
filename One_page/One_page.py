
import reflex as rx

from Navbar_trasparente import Navbar_trasparente
from Cabezera import Fondo_fijo
from Nuestra_cocina import tres_fotos_pequenas 
from Carrusel_foto_grande import Carrusel_grande
from Compromiso import Compromiso 
from Carrusel_foto_pequena import Carrusel_peque
from Footer import UbicacionFooter



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
                        Fondo_fijo(),
                        tres_fotos_pequenas(),
                        Carrusel_grande(),
                        Compromiso(),
                        Carrusel_peque(),
                        UbicacionFooter(),
                        


                    )

    


app = rx.App()
app.add_page(index)
