from sqlalchemy import select
from models import Pedido
from database import engine

def read_pedidos():
    query = select(Pedido)
    with engine.connect() as connection:
        result = connection.execute(query)
        pedidos = result.fetchall()
        return pedidos