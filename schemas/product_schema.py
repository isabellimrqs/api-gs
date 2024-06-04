from typing import Optional
from pydantic import BaseModel as SCBaseModel

class ProductSchema(SCBaseModel):
    
    id_producto: Optional[int] = None
    status: str | None
    modelo_herramienta: str 
    codigo_herramienta: str 
    categoria1: str 
    categoria2: str 
    nombre_producto: str 
    voltaje: str 
    codigo_barras: float 
    pais_origen: str 
    largo_individual: float 
    ancho_individual: float  
    alto_individual: float  
    largo_master: float  
    ancho_master: float  
    alto_master: float | None
    cantidad_herramientas_empaque_master: float | None
    peso_individual: float  
    peso_empaque_master: float  
    potencia_w: str  
    garantia: str | None 
    argumentos_ventas: str  
    nombre_producto_descripcion_corta: str  
    contenido_del_empaque: str  
    aplicaciones: str  
    materiales_puede_trabajar: str
    crear_o_reparar: str
    velocidadRPM: str
    family_group: str
    compatible: str
    imagenes: str 
    tiene_video: str 
    cuantos: float
    link_youtube: str

class Config:
    orm_mode = True