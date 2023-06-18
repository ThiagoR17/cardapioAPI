from sqlalchemy import select
from models import pedidos
from database import engine

def read_pedidos():
    query = select(pedidos)
    with engine.connect() as connection:
        result = connection.execute(query)
        pedidos = result.fetchall()
        return pedidos