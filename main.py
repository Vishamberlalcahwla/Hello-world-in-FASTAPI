from re import A
from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def hello_alnafi_students():
    return "I am student of devops track"

