from typing import Union
import datetime
from fastapi import FastAPI, Response
import time

app = FastAPI()


@app.get("/")
def read_root():
    time.sleep(10)
    return {"Hello": "World", 'time': datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}