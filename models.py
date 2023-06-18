from decimal import Decimal
from pydantic import BaseModel
from typing import List, Optional


class Pedido(BaseModel):
    idpedidos: int
    valor_pedido: float
    pedido: str


class mesa(BaseModel):
    idmesa: int
    nome_cliente: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            Decimal: lambda v: str(v)  # Serialize Decimal as string
        }