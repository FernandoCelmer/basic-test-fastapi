# [project-basic-test-fastapi]

![GitHub last commit](https://img.shields.io/github/last-commit/FernandoCelmer/project-basic-test-fastapi)
![GitHub followers](https://img.shields.io/github/followers/FernandoCelmer?label=Fernando%20Celmer&style=social)

## Sobre
Este repositório contém um projeto Python básico de uma API desenvolvido com o framework fastapi.

## 🚀 Technologies

- [Python](https://www.python.org/) 
- [FastAPI](https://fastapi.tiangolo.com/)
- [Docker](https://docs.docker.com/)

# Instruções
## Excutando o Projeto Local [PIP]

<details>
  <summary>List of required commands</summary>

 - Crie um novo ambiente virtual Python
```bash
virtualenv -p python3.9 venv
```
 - Ative o ambiente virtual
```bash
source venv/bin/activate
```
 - Instale os requerimentos com o PIP
```bash
pip install -r requirements.txt
```
 - Execute a aplicação
```
uvicorn app.main:app --host 0.0.0.0 --reload
```

 </details>


## Excutando o Projeto Local [Poetry]

  <details>
  <summary>List of required commands</summary>
 
 - Instalando Poetry
 ```
 curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
 ```

  - Ative o ambiente virtual
```bash
poetry shell
```
 - Instale os requerimentos
```bash
poetry install
```

 </details>
   
## Executando o projeto com [Docker]

<details>
  <summary>List of required commands</summary>
 
 - Construindo a imagem Docker

```bash
sudo docker build --tag fastapi/dev --file docker/Dockerfile .
```

 - Iniciando o contêiner Docker

```bash
sudo docker run --name my_fastapi -d -p 80:80 fastapi/dev
```

 </details>
