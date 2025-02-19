@echo off

if not defined HOST set HOST=127.0.0.1
if not defined PORT set PORT=5000

if "%1" == "dev" (
    call .venv\Scripts\activate
    python server.py
) else (
    call .venv\Scripts\activate
    waitress-serve --host %HOST% --port %PORT% server:app
)

