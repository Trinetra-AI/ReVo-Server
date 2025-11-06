from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from firebase_admin_setup import db
import uvicorn

app = FastAPI(title="ReVo Firebase Server")

class User(BaseModel):
    username: str
    email: str | None = None
    gold: int | None = 0
    skins: dict | None = {}

@app.get("/")
def read_root():
    return {"message": "ReVo Firebase Server (FastAPI) — Running ✅"}

@app.post("/add_user")
def add_user(user: User):
    # Convert Pydantic model to dict
    data = user.dict()
    doc_ref = db.collection("users").add(data)
    return {"status": "success", "doc_id": doc_ref[1].id, "data": data}

@app.get("/get_users")
def get_users():
    try:
        docs = db.collection("users").stream()
        results = [{doc.id: doc.to_dict()} for doc in docs]
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info")
