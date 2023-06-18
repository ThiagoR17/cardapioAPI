from fastapi import FastAPI
from models import mesa
from database import SessionLocal

app = FastAPI()

@app.get("/mesas/")
def create_mesa(mesa: mesa):
    
    return {"OLA"}

@app.get("/mesas/")
def read_mesas():
    db = SessionLocal()
    mesas = db.query(mesa).all()
    return mesas

@app.get("/mesas/{mesa_id}")
def read_mesa(mesa_id: int):
    db = SessionLocal()
    mesa = db.query(mesa).filter(mesa.idmesas == mesa_id).first()
    if mesa:
        return mesa
    return {"error": "Mesa não encontrada!"}

@app.put("/mesas/{mesa_id}")
def update_mesa(mesa_id: int, updated_mesa: mesa):
    db = SessionLocal()
    mesa = db.query(mesa).filter(mesa.idmesas == mesa_id).first()
    if mesa:
        mesa.nome_cliente = updated_mesa.nome_cliente
        mesa.pedidos_idpedidos = updated_mesa.pedidos_idpedidos
        db.commit()
        return mesa
    return {"error": "Mesa not found"}

@app.delete("/mesas/{mesa_id}")
def delete_mesa(mesa_id: int):
    db = SessionLocal()
    mesa = db.query(mesa).filter(mesa.idmesas == mesa_id).first()
    if mesa:
        db.delete(mesa)
        db.commit()
        return {"message": "Mesa deleted"}
    return {"error": "Mesa not found"}