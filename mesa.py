from fastapi import FastAPI
from models import Mesa
from database import SessionLocal

app = FastAPI()

@app.post("/mesas/")
def create_mesa(mesa: Mesa):
    db = SessionLocal()
    db.add(mesa)
    db.commit()
    db.refresh(mesa)
    return mesa

@app.get("/mesas/")
def read_mesas():
    db = SessionLocal()
    mesas = db.query(Mesa).all()
    return mesas

@app.get("/mesas/{mesa_id}")
def read_mesa(mesa_id: int):
    db = SessionLocal()
    mesa = db.query(Mesa).filter(Mesa.idmesas == mesa_id).first()
    if mesa:
        return mesa
    return {"error": "Mesa not found"}

@app.put("/mesas/{mesa_id}")
def update_mesa(mesa_id: int, updated_mesa: Mesa):
    db = SessionLocal()
    mesa = db.query(Mesa).filter(Mesa.idmesas == mesa_id).first()
    if mesa:
        mesa.nome_cliente = updated_mesa.nome_cliente
        mesa.pedidos_idpedidos = updated_mesa.pedidos_idpedidos
        db.commit()
        return mesa
    return {"error": "Mesa not found"}

@app.delete("/mesas/{mesa_id}")
def delete_mesa(mesa_id: int):
    db = SessionLocal()
    mesa = db.query(Mesa).filter(Mesa.idmesas == mesa_id).first()
    if mesa:
        db.delete(mesa)
        db.commit()
        return {"message": "Mesa deleted"}
    return {"error": "Mesa not found"}