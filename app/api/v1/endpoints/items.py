from typing import List
from sqlalchemy.orm import Session

from fastapi import Depends, Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.controllers.item import ControlerItem
from app.schemas.item import SchemaItem
from app.database import get_db


router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/items", response_model=List[SchemaItem])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    operation = ControlerItem(db=db)
    return operation.get_all()


@router.get("/items/{id}", response_model=SchemaItem)
def read_item(id: str, db: Session = Depends(get_db)):
    operation = ControlerItem(db=db)
    return operation.get(model_id=id)


@router.get("/view_item/{id}", response_class=HTMLResponse)
async def view_item(request: Request, id: str, db: Session = Depends(get_db)):
    operation = ControlerItem(db=db)
    item = operation.get(model_id=id)

    return templates.TemplateResponse(
        "item.html",
        {
            "request": request,
            "id": item.id,
            "title": item.title,
            "description": item.description
        }
    )
