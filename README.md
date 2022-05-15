# [project-basic-test-fastapi]

![GitHub last commit](https://img.shields.io/github/last-commit/FernandoCelmer/project-basic-test-fastapi)
![GitHub followers](https://img.shields.io/github/followers/FernandoCelmer?label=Fernando%20Celmer&style=social)

## Sobre
Este repositório contém um projeto Python básico de uma API desenvolvido com o framework fastapi.

## 🚀 Technologies

- [Python](https://www.python.org/) 
- [FastAPI](https://fastapi.tiangolo.com/)
- [Docker](https://docs.docker.com/)

## Construindo a imagem Docker
Vá para o diretório do projeto (onde Dockerfile está, contendo seu app diretório).
Crie sua imagem FastAPI:

```bash
sudo docker build --tag fastapi/dev --file docker/Dockerfile .
```

## Iniciando o contêiner Docker

```bash
sudo docker run -d -p 80:80 fastapi/dev
```
