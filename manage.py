import os
import subprocess
from pathlib import Path

import typer
import uvicorn
from PyInstaller import __main__ as pyi

main = typer.Typer()

CUR_PATH = Path(__file__).resolve().parent


@main.command()
def start(
    reload: bool = typer.Option(False, "--reload", "-r", help="auto reload"),
    port: int = typer.Option(8000, "--port", "-p", help="workers"),
    workers: int = typer.Option(1, "--workers", "-w", help="workers"),
):
    from backend.app import app

    uvicorn.run(app, host="0.0.0.0", port=port, reload=reload, workers=workers)


@main.command()
def install():
    os.chdir(CUR_PATH / "frontend")
    subprocess.run(["pnpm", "install"], check=True)


@main.command()
def dev():
    os.chdir(CUR_PATH / "frontend")
    subprocess.run(["pnpm", "run", "dev"], check=True)


@main.command()
def build():
    os.chdir(CUR_PATH / "frontend")
    subprocess.run(["pnpm", "run", "build"], check=True)
    os.chdir(CUR_PATH)
    if not (CUR_PATH / "main.spec").exists():
        pyi.run(["-F", "--add-data", "public:public", "main.py"])
    pyi.run(["main.spec"])


if __name__ == "__main__":
    main()
