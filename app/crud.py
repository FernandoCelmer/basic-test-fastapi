from sqlalchemy.orm import Session

from app.models.item import Item
from app.schemas.item import SchemaItemCreate


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()

def get_item(db, id):
    return db.query(Item).filter(
        Item.id == id
    ).first()

def create_item(db: Session, item: SchemaItemCreate):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
