### 🌦️ Weather Facts API 🌦️

This project provides a simple **Flask API** that returns random weather facts. The API exposes a single endpoint `/fact` that returns a JSON object with a random weather fact.

---

### 📦 Requirements 📦
- `Python 3.0` or above.
- `pip` for installing dependencies.
### 🛠️ Installation 🛠️
```sh
git clone https://github.com/4475f9e4-1337-4c5b-bc13-6534b2c3a92d/weather_facts.git && cd weather_facts
```
### ⚙️ Build ⚙️
##### Using Makefile:
```sh
make build
```
##### Without Makefile:
###### For **Linux/macOS**:
```sh
python -m venv .venv
. .venv/bin/activate
pip install .
```
###### For **Windows**:
```sh
python -m venv .venv
. .venv/Scripts/activate
pip install .
```
---
### 🚀 Running the Server 🚀
##### Development:
To run the server in development mode:
```sh
./run.sh dev
``` 
or directly:
```sh
python server.py
```
##### Production:
To run the server in production mode using `waitress-serve`:
```sh
./run.sh
```
##### Custom Host/Port:
To specify a custom host and port, set the `HOST` and `PORT` environment variables:
```sh
HOST=0.0.0.0 PORT=8080 ./run.sh
```
---
### 📝 Usage 📝
##### Request:
To get a random weather fact, send a `GET request` to the `/fact` endpoint:

```sh
curl -s http://127.0.0.1:5000/fact
```
##### Response:
The response will return a random weather fact in JSON format:
```JSON
{ "fact": "A 2003 heatwave turned grapes to raisins before they were picked from the vine!" }
```

