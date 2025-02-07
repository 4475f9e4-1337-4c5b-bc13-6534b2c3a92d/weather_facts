#!/bin/sh

if [ "$(uname)" = "Darwin" ] || [ "$(uname)" = "Linux" ]; then
    . .venv/bin/activate
else
    . .venv/Scripts/activate
fi

if [ "$1" = "dev" ]; then
    python server.py
else
    exec waitress-serve --host "${HOST:-127.0.0.1}" --port "${PORT:-5000}" server:app
fi


