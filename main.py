from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from temscale import temscale

app = FastAPI()


origins = [
    "*",
    "http://127.0.0.1:8000/",
    "http://127.0.0.1/",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TemscaleModel(BaseModel):
    value: int
    old_type: str
    new_type: str


@app.post("/convert")
async def convert(temscale_model: TemscaleModel):
    try:
        tem = temscale.Temscale(temscale_model.value, temscale_model.old_type)
        tem.convert(temscale_model.new_type)
        return temscale.to_dict(tem)
    except TypeError:
        return HTTPException(status_code=400, detail="Invalid type")
