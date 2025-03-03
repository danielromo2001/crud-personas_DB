from fastapi import FastAPI, HTTPException


app = FastAPI()

@app.get("/")

def read_root():
    return {"messege": "This is the root page of the API"}

