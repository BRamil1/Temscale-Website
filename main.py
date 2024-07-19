from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()


@app.get("/", )
async def root():
    return Response("website/index.html")


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
