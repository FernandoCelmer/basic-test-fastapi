from typing import List
from sqlalchemy.orm import Session

from fastapi import Depends, Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app import crud, models, schemas
from app.database import engine, get_db

models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@router.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@router.get("/items/{id}", response_model=schemas.Item)
def read_item(id: str, db: Session = Depends(get_db)):
    item = crud.get_item(db=db, id=id)
    return item

@router.get("/view_item/{id}", response_class=HTMLResponse)
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
