from core.configs import settings
from sqlalchemy import Column, Integer, String, Float

class ProductModel(settings.DBBaseModel):
    __tablename__ = 'dbo.dremel'

    status: str = Column(String(30))
    modelo_herramienta: str = Column(String(100))
    codigo_herramienta: str = Column(String(100))
    categoria1: str = Column(String(100))
    categoria2: str = Column(String(100))
    nombre_producto: str = Column(String(100))
    voltaje: str = Column(String(100))
    codigo_barras: str = Column(Float)
    pais_origen: str = Column(String(100)) 
    largo_individual: str = Column(Float) 
    ancho_individual: str = Column(Float)  
    alto_individual: str = Column(Float)  
    largo_master: str = Column(Float)  
    ancho_master: str = Column(Float)  
    alto_master: str = Column(Float)  
    cantidad_herramientas_empaque_master: str = Column(Float)  
    peso_individual: str = Column(Float)  
    peso_empaque_master: str = Column(Float)  
    potencia_w: str = Column(String(100))  
    garantia: str = Column(String(100))  
    argumentos_ventas: str = Column(String(100))  
    nombre_producto_descripcion_corta: str = Column(String(100))  
    contenido_del_empaque: str = Column(String(100))  
    aplicaciones: str = Column(String(100))  
    materiales_puede_trabajar: str = Column(String(100))
    crear_o_reparar: str = Column(String(100))
    velocidadRPM: str = Column(String(100))
    family_group: str = Column(String(100))
    compatible: str = Column(String(100))
    imagenes: str = Column(String(255))
    tiene_video: str = Column(String(255))
    cuantos: str = Column(Float)
    link_youtube: str = Column(Float)
    id_producto: int = Column(Integer, primary_key=True)

    

