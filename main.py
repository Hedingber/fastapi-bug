import asyncio
from pathlib import Path

from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/")
def store_log(request: Request):
    body = asyncio.run(request.body())
    log_file = Path(f'./output.txt')
    with log_file.open('ab') as file:
        file.write(body)
    return None
