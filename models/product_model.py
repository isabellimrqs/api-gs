from core.configs import settings
from sqlalchemy import Column, Integer, String, Float

class ProductModel(settings.DBBaseModel):
    __tablename__ = 'dremel'

    id_producto: int = Column(Integer, primary_key=True)
    status: str = Column(String(30))
    modelo_herramienta: str = Column(String(100))
    codigo_herramienta: str = Column(String(100))
    categoria1: str = Column(String(100))
    categoria2: str = Column(String(100))
    nombre_producto: str = Column(String(100))
    voltaje: str = Column(String(100))
    codigo_barras: float = Column(Float)
    pais_origen: str = Column(String(100)) 
    largo_individual: float = Column(Float) 
    ancho_individual: float = Column(Float)  
    alto_individual: float = Column(Float)  
    largo_master: float = Column(Float)  
    ancho_master: float = Column(Float)  
    alto_master: float = Column(Float)  
    cantidad_herramientas_empaque_master: float = Column(Float)  
    peso_individual: float = Column(Float)  
    peso_empaque_master: float = Column(Float)  
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
    cuantos: float = Column(Float)
    link_youtube: str = Column(String(255))

    

