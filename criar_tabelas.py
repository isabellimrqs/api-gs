import asyncio
from core.database import engine
from core.configs import settings
import models.all_models  

async def create_tables() -> None:
    print("Criando tabelas...")
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print('Tabelas criadas com sucesso!')

if __name__ == '__main__':
    asyncio.run(create_tables())
