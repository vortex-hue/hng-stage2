from fastapi import FastAPI, Depends, Response, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from typing import List
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import schema, models, database, person

app = FastAPI()

# Set allowed origins
origins = ["https://stage2.up.railway.app", '*']

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

router = APIRouter(
    prefix='/api',
    tags=["Persons"]
)

models.Person.metadata.create_all(database.engine)



def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("", response_model=List[schema.Person])
async def get_all_persons(db: Session = Depends(get_db)):
    return person.all(db)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_person(request: schema.Person, db: Session = Depends(get_db)):
    return person.create(request, db)


@router.get("/{id}", response_model=schema.Person)
async def get_person_by_id(id, db: Session = Depends(get_db)):
    return person.show(id, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_person(id, db: Session = Depends(get_db)):
    return person.destroy(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_person(id, request: schema.Person, db: Session = Depends(get_db)):
    return person.update(id, request, db)

app.include_router(router)
## debug mode
# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=5000)
