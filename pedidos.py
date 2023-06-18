from fastapi import FastAPI
from models import Pedido, mesa
from database import SessionLocal


app = FastAPI()
@app.post("/pedidos")
def create_pedido(pedido: Pedido):
    db = SessionLocal()
    db.add(pedido)
    db.commit()
    db.refresh(pedido)

    return pedido
@app.get("/pedidos")
def read_pedidos():
    db = SessionLocal()
    pedidos = db.query(Pedido).all()
    return pedidos

@app.get("/pedidos/{pedido_id}")
def read_pedido(pedido_id: int):
    db = SessionLocal()
    pedido = db.query(Pedido).filter(Pedido.idpedidos == pedido_id).first()
    if pedido:
        return pedido
    return {"error": "Pedido not found"}

@app.put("/pedidos/{pedido_id}")
def update_pedido(pedido_id: int, updated_pedido: Pedido):
    db = SessionLocal()
    pedido = db.query(Pedido).filter(Pedido.idpedidos == pedido_id).first()
    if pedido:
        pedido.valor_pedido = updated_pedido.valor_pedido
        pedido.pedido = updated_pedido.pedido
        db.commit()
        return pedido
    return {"error": "Pedido not found"}
