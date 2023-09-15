from fastapi import Depends, Response, HTTPException, status
from typing import List

import database, models
import schema
from sqlalchemy.orm import Session


get_db = database.get_db


def all(db : Session = Depends(get_db)):
    persons = db.query(models.Person).all()
    return persons

def create(request: schema.Person, db : Session = Depends(get_db)):
    new_person = models.Person(name=request.name, email=request.email, age=request.age)
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    return new_person

def show(id, db : Session = Depends(get_db)):
    person = db.query(models.Person).filter(models.Person.id == id).first()
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The person with the id {id} is not found in the Database")
    return person

def destroy(id, db : Session = Depends(get_db)):
    db.query(models.Person).filter(models.Person.id == id).delete(synchronize_session=False)
    db.commit()
    return {'Message': f'person with  id "{id}" is deleted'}


def update(id, request: schema.Person,  db : Session = Depends(get_db)):
    person = db.query(models.Person).filter(models.Person.id == id).update({'name': request.name, 'age': request.age, 'email': request.email}, synchronize_session='evaluate')
    if not person:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f'person with id {id} is not available in the database')
    db.commit()
    return {'message': f'{request.name} is updated successfully'}