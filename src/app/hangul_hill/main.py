from fastapi import FastAPI
import uvicorn
from starlette.staticfiles import StaticFiles

from app.hangul_hill.api.api_v1.route import api_v1_route
from app.hangul_hill.utils.exceptions.exception_handler import include_exception
from app.hangul_hill.api.index.route import index_route
app = FastAPI(title = "Hangul Hill cipher",
             description = "Hangul Hill cipher is hrabit64(Junser Hwang)'s Toy project for linear algebra project",
             version = "0.1.0")

app.include_router(api_v1_route)
app.include_router(index_route)
include_exception(app)
app.mount("/static", StaticFiles(directory="resource/static"), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=18000, log_level="debug")
