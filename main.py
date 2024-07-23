from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from temscale import temscale

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TemscaleModel(BaseModel):
    value: float
    old_type: str
    new_type: str


@app.post("/convert")
async def convert(temscale_model: TemscaleModel):
    """Accepts data, old type and new type of temperature and returns already converted to the new type"""
    try:
        tem = temscale.Temscale(temscale_model.value, temscale_model.old_type)
        tem.convert(temscale_model.new_type)
        return temscale.to_dict(tem)
    except TypeError:
        return HTTPException(status_code=400, detail="Invalid type")
