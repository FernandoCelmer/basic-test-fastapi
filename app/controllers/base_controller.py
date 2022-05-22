# coding=utf-8

from app import database
from app.database import engine

from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

database.Base.metadata.create_all(bind=engine)


class BaseController(object):
    """ Base View to create helpers common to all Webservices.
    """
    def __init__(self, db: Session, data: dict = {}):
        """
        Constructor
        """

        self.close_session = None
        if db:
            self.db = db
        else:
            self.db = Session(engine)
            self.close_session = True

        self.data = data
        self.model_class = None
    

    def get_all(self):
        """
        Method GET All
        """

        try:
            query = self.db.query(self.model_class).all()

            if query:
                return query

        except Exception as error:
            print(error)
            return JSONResponse(status_code=500)

        finally:
            if self.close_session:
                self.db.close()

        return JSONResponse(status_code=404)


    def get(self, model_id: int):
        """
        Method GET
        """

        try:
            query = self.db.query(self.model_class) \
                .filter( self.model_class.id == model_id).first()
            
            if query:
                return query

        except Exception as error:
            print(error)
            return JSONResponse(status_code=500)

        finally:
            if self.close_session:
                self.db.close()

        return JSONResponse(status_code=404)
