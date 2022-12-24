from typing import Optional

from starlette.config import Config
from authlib.integrations.starlette_client import OAuth, OAuthError
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
import requests
import json
import uvicorn
import os
from datetime import datetime

from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request

from starlette.responses import RedirectResponse, JSONResponse

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    try:
        os.makedirs('output')
    except:
        pass

origins = [
  "*"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["POST", "GET"],
  allow_headers=["*"],
)


@app.get("/")
async def check(request: Request):
    return JSONResponse({"message": "200"})

@app.post("/")
async def send_msg(request: Request):
    try:
        payload = await request.json()
        from_address = (request.client.__str__())
        headers = (request.headers.__str__())
        print(datetime.timestamp(datetime.now()))
        with open(f'output/{datetime.timestamp(datetime.now())}.txt', 'w') as output_buffer:
            print(payload, file=output_buffer)
            print(from_address, file=output_buffer)
            print(headers, file=output_buffer)
            # output_buffer.write(payload)
        return JSONResponse({"message": "200"})
    except:
        return JSONResponse({"message": "500"})



if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info",
              reload=True)