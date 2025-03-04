from fastapi import FastAPI, HTTPException
from model.user_connection import UserConnection
from schema.user_schema import UserSchema


app = FastAPI()
conn = UserConnection()

@app.get("/") #Aca se muestra la lista de usuarios guardados en la BD
def root():
    items = []
    for data in conn.read_all():
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["name"] = data[1]
        dictionary["phone"] = data[2]
        items.append(dictionary)
    return items

@app.get("/users/{id}") #Aca se muestra un usuario en especifico que esta almacenado en la BD
def read_one(id:str):
    data = conn.read_one(id)
    if data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    dictionary = {}
    dictionary["id"] = data[0]
    dictionary["name"] = data[1]
    dictionary["phone"] = data[2]
    return dictionary


@app.post("/users/insert") #Aca hacemos un inset de un usuario a nuestra BD
def insert(user_data: UserSchema):
    data = user_data.dict()
    data.pop("id")
    conn.write(data)
    return {"messege": "Data inserted successfully"}


@app.put("/users/update/{id}") #Aca actualizamos un usuario en especifico que esta almacenado en la BD
def update(id: str, user_data: UserSchema):
    data = user_data.dict()
    data["id"] = id  # Añadir el id al diccionario de datos
    conn.update(data)
    return {"message": "Data updated successfully"}


@app.delete("/users/delete/{id}")
def delete(id:str):
    conn.delete(id)
    return {"messege": "Data deleted successfully"}


