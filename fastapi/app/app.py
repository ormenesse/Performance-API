from typing import Union
import datetime
from fastapi import FastAPI
import time

app = FastAPI()


@app.get("/")
async def read_root():
    time.sleep(10)
    return {"Hello": "World", 'time': datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}