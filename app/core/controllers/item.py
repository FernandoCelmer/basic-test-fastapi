# coding=utf-8

from app.core.models.item import Item
from app.settings.controller import BaseController

from sqlalchemy.orm import Session


class ControlerItem(BaseController):
    """
    Controller Item
    """
    def __init__(self, db: Session, data: dict = {}):
        super().__init__(db, data)

        self.model_class = Item