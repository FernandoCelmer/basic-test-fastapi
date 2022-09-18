from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.settings.config import ROOT_PATH
from app.api.v1.routers import router
from mangum import Mangum


app = FastAPI(
    title="Fastapi",
    description="Project Basic Test Fastapi",
    version="0.0.1",
    contact={
        "name": "Fernando Celmer",
        "email": "email@fernandocelmer.com"
    },
    root_path=ROOT_PATH
)

app.include_router(router, prefix="/v1")

app.mount("/app/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/static/templates")


@app.get("/index", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "message": "project-basic-test-fastapi"
        }
    )


@app.get("/status")
def get_status():
    """Get status of messaging server."""
    return ({"status":  "it's alive"})


handler = Mangum(app)