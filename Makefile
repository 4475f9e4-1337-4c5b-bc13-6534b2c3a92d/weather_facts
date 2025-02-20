.PHONY: build run clean

VENV = .venv

# Detect OS
ifeq ($(OS), Windows_NT)
    ACTIVATE = $(VENV)\\Scripts\\activate
else
    ACTIVATE = . $(VENV)/bin/activate
endif

build:
ifeq ($(OS), Windows_NT)
	@if not exist "$(VENV)" python -m venv $(VENV)
else
	@if [ ! -d "$(VENV)" ]; then python -m venv $(VENV); fi
endif
	@$(ACTIVATE) && pip install .
	@echo "Build complete."

run:
	@$(ACTIVATE) && waitress-serve --host 127.0.0.1 --port 5000 server:app

clean:
ifeq ($(OS), Windows_NT)
	@if exist "$(VENV)" rmdir /s /q "$(VENV)"
	@if exist "build" rmdir /s /q "build"
	@if exist "weather_facts.egg-info" rmdir /s /q "weather_facts.egg-info"
	@if exist "favorites.json" del /q "favorites.json"
else
	@rm -rf $(VENV)
	@rm -rf build
	@rm -rf weather_facts.egg-info
	@rm -f favorites.json
endif
	@echo "Clean complete."

