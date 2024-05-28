from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
# from core.database import SessionLocal
from schemas.product_schema import ProductSchema
from models.all_models import ProductModel
from core.deps  import get_session
from typing import List

app = FastAPI()

# async def get_db():
#     async with SessionLocal() as session:
#         yield session

#response_model=List[ProductSchema]
@app.get("/products/", response_model=List[ProductSchema] )
async def get_products(db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(ProductModel))
    products = result.scalars().all()
    print(result)
    return products

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
