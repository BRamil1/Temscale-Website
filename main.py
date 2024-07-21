from fastapi import FastAPI, HTTPException, Form
from pydantic import BaseModel
from temscale import temscale
from typing import Annotated

app = FastAPI()


class TemscaleModel(BaseModel):
    value: int
    old_type: str
    new_type: str


@app.post("/convert_json")
async def convert(temscale_model: TemscaleModel):
    try:
        tem = temscale.Temscale(temscale_model.value, temscale_model.old_type)
        tem.convert(temscale_model.new_type)
        return temscale.to_dict(tem)
    except TypeError:
        return HTTPException(status_code=400, detail="Invalid type")


@app.post("/convert")
async def convert(value: Annotated[int, Form()],
                  old_type: Annotated[str, Form()],
                  new_type: Annotated[str, Form()]):
    try:
        tem = temscale.Temscale(value, old_type)
        tem.convert(new_type)
        return temscale.to_dict(tem)
    except TypeError:
        return HTTPException(status_code=400, detail="Invalid type")
