from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from temscale import temscale

app = FastAPI()


class TemscaleModel(BaseModel):
    value: int
    type: str


@app.post("/convert")
async def convert(temscale_model: TemscaleModel, new_type: str):
    try:
        tem = temscale.Temscale(temscale_model.value, temscale_model.type)
        tem.convert(new_type)
        return temscale.to_dict(tem)
    except TypeError:
        return HTTPException(status_code=400, detail="Invalid type")
