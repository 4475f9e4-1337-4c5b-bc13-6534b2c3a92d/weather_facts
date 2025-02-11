.PHONY: build run clean

VENV = .venv

# Detect OS
ifeq ($(OS), Windows_NT)
    ACTIVATE = $(VENV)\Scripts\activate
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
	@rmdir /s /q $(VENV)
	@rmdir /s /q build
	@rmdir /s /q weather_facts.egg-info
else
	@rm -rf $(VENV)
	@rm -rf build
	@rm -rf weather_facts.egg-info
endif
	@echo "Clean complete."

