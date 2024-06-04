from fastapi import FastAPI, Depends, status, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from schemas.product_schema import ProductSchema
from models.all_models import ProductModel
from core.deps import get_session
from typing import List

app = FastAPI(title="FAQ GS",summary="Plataforma de preguntas frecuentes (Preguntas Frecuentes) sobre productos Bosch para GS/OBC" )

@app.post("/products/", status_code=status.HTTP_201_CREATED, response_model=ProductSchema )
async def post_product(product: ProductSchema,  db: AsyncSession = Depends(get_session)):
        new_product = ProductModel(status = product.status, 
                                   modelo_herramienta = product.modelo_herramienta, 
                                   codigo_herramienta = product.codigo_herramienta, 
                                   categoria1 = product.categoria1, 
                                   categoria2 = product.categoria2, 
                                   nombre_producto = product.nombre_producto, 
                                   voltaje = product.voltaje,  
                                   codigo_barras = product.codigo_barras, 
                                   pais_origen = product.pais_origen, 
                                   largo_individual = product.largo_individual,  
                                   ancho_individual = product.ancho_individual, 
                                   alto_individual = product.alto_individual, 
                                   largo_master = product.largo_master,  
                                   ancho_master = product.ancho_master, 
                                   cantidad_herramientas_empaque_master = product.cantidad_herramientas_empaque_master,  peso_individual = product.peso_individual, 
                                   peso_empaque_master = product.peso_empaque_master, 
                                   potencia_w = product.potencia_w, 
                                   garantia = product.garantia, 
                                   argumentos_ventas = product.argumentos_ventas, 
                                   nombre_producto_descripcion_corta = product.nombre_producto_descripcion_corta, contenido_del_empaque = product.contenido_del_empaque, 
                                   aplicaciones = product.aplicaciones, 
                                   materiales_puede_trabajar = product.materiales_puede_trabajar, 
                                   crear_o_reparar = product.crear_o_reparar, 
                                   velocidadRPM = product.velocidadRPM, 
                                   family_group = product.family_group, 
                                   compatible = product.compatible, 
                                   imagenes = product.imagenes, 
                                   tiene_video = product.tiene_video, 
                                   cuantos = product.cuantos, 
                                   link_youtube = product.link_youtube)
        db.add(new_product)
        await db.commit()

        return new_product

@app.get("/products/", response_model=List[ProductSchema], status_code=status.HTTP_200_OK )
async def get_products(db: AsyncSession = Depends(get_session)):
        result = await db.execute(select(ProductModel))
        products = result.scalars().all()
        print(result)
        return products

@app.get("/products/{product_id}", response_model=ProductSchema, status_code=status.HTTP_200_OK )
async def get_product(product_id: int,  db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProductModel).filter(ProductModel.id_producto == product_id)
        result = await session.execute(query)
        product = result.unique().scalar_one_or_none()

        if product:
            return product
        else:
            raise HTTPException(detail="Producto no encontrado", status_code=status.HTTP_404_NOT_FOUND)
        

@app.put("/products/{product_id}", response_model=ProductSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_product(product_id: int, product: ProductSchema, db: AsyncSession = Depends(get_session)):
     async with db as session:
          query = select(ProductModel).filter(ProductModel.id_producto == product_id)
          result = await session.execute(query)
          update_product = result.unique().scalar_one_or_none()

          if update_product:
               update_product.status = product.status
               update_product.modelo_herramienta = product.modelo_herramienta
               update_product.codigo_herramienta = product.codigo_herramienta
               update_product.categoria1 = product.categoria1
               update_product.categoria2 = product.categoria2
               update_product.nombre_producto = product.nombre_producto
               update_product.voltaje = product.voltaje
               update_product.codigo_barras = product.codigo_barras
               update_product.pais_origen = product.pais_origen
               update_product.largo_individual = product.largo_individual
               update_product.ancho_individual = product.ancho_individual
               update_product.alto_individual = product.alto_individual
               update_product.largo_master = product.largo_master
               update_product.ancho_master = product.ancho_master
               update_product.cantidad_herramientas_empaque_master = product.cantidad_herramientas_empaque_master
               update_product.peso_individual = product.peso_individual
               update_product.peso_empaque_master = product.peso_empaque_master
               update_product.potencia_w = product.potencia_w
               update_product.garantia = product.garantia
               update_product.argumentos_ventas = product.argumentos_ventas
               update_product.nombre_producto_descripcion_corta = product.nombre_producto_descripcion_corta
               update_product.contenido_del_empaque = product.contenido_del_empaque
               update_product.aplicaciones = product.aplicaciones
               update_product.materiales_puede_trabajar = product.materiales_puede_trabajar
               update_product.crear_o_reparar = product.crear_o_reparar
               update_product.velocidadRPM = product.velocidadRPM
               update_product.family_group = product.family_group
               update_product.compatible = product.compatible
               update_product.imagenes = product.imagenes
               update_product.tiene_video = product.tiene_video
               update_product.cuantos = product.cuantos
               update_product.link_youtube = product.link_youtube
          else:
               raise HTTPException(detail="Product no encontrado", status_code=status.HTTP_404_NOT_FOUND)
            
        

@app.delete('/products/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int, db: AssertionError = Depends(get_session)):
     async with db as session:
          query = select(ProductModel).filter(ProductModel.id_producto == product_id)
          result = await session.execute(query)
          delete_product = result.unique().scalar_one_or_none()

          if delete_product:
               await session.delete(delete_product)
               await session.commit()
               return Response(status_code=status.HTTP_204_NO_CONTENT)
          else: 
                raise HTTPException(detail="Producto no encontrado", status_code=status.HTTP_404_NOT_FOUND)
        


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
