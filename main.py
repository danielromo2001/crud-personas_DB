from fastapi import FastAPI, HTTPException
from model.user_connection import UserConnection
from schema.user_schema import UserSchema


app = FastAPI()
conn = UserConnection()

@app.get("/")
def root():
    conn 
    return {"messege": "This is the root page of the API"}

@app.post("/users/insert")
def insert(user_data: UserSchema):
    data = user_data.dict()
    data.pop("id")
    conn.write(data)

