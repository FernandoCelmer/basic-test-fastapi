# [project-basic-test-fastapi]

![GitHub last commit](https://img.shields.io/github/last-commit/FernandoCelmer/project-basic-test-fastapi)
![GitHub followers](https://img.shields.io/github/followers/FernandoCelmer?label=Fernando%20Celmer&style=social)

## Sobre
This repository contains a basic Python project of an API developed with the fastapi framework.

## 🚀 Stack

- [Python](https://www.python.org/) 
- [FastAPI](https://fastapi.tiangolo.com/)
- [Docker](https://docs.docker.com/)

# Instructions
## Running the Local Project with [PIP]

 - Create a new Python virtual environment
```bash
virtualenv -p python3.9 venv
```
 - Activate the virtual environment
```bash
source venv/bin/activate
```
 - Install requirements with PIP
```bash
pip install -r requirements.txt
```
 - Run the application
```
uvicorn app.main:app --host 0.0.0.0 --reload
```
## Running the Local Project with [Poetry]
 - Installing Poetry
 ```
 curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
 ```

  - Activate the virtual environment
```bash
poetry shell
```
 - install the requirements
```bash
poetry install
```

## Running the project with [Docker]

 - Building the Docker image

```bash
sudo docker build --tag fastapi/dev --file docker/Dockerfile .
```

 - Starting the Docker container

```bash
sudo docker run --name my_fastapi -d -p 80:80 fastapi/dev
```
