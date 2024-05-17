from typing import Optional
from pydantic import BaseModel

class Produto(BaseModel):
    id_produto: Optional[int] = None
    status: str
    

