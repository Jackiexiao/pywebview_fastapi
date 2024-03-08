from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

ROOT_PATH = Path(__file__).parent.parent
public_file_abspath = ROOT_PATH / "public"

app.mount("/", StaticFiles(directory=str(public_file_abspath)), name="public")


@app.get("/api")
def index():
    return JSONResponse({"status": 200, "msg": "ok"})
