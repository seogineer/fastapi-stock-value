from Scrap import Scrap

from fastapi import FastAPI
from pydantic import BaseModel


class Request(BaseModel):
    ticker: str
    start: str
    end: str


app = FastAPI()


@app.post("/stock/")
async def get_stock(req: Request):
    return Scrap.get_stock(req.ticker, req.start, req.end)
