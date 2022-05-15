from typing import List

from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from . import crud, models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "message": "project-basic-test-fastapi"
        }
    )

@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@app.get("/items/{id}", response_model=schemas.Item)
def read_item(id: str, db: Session = Depends(get_db)):
    item = crud.get_item(db=db, id=id)
    return item

@app.get("/view_item/{id}", response_class=HTMLResponse)
async def view_item(request: Request, id: str, db: Session = Depends(get_db)):
    teste = crud.get_item(db=db, id=id)
    return templates.TemplateResponse(
        "item.html",
        {
            "request": request,
            "id": teste.id,
            "title": teste.title,
            "description": teste.description
        }
    )
