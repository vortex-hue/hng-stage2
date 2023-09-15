from fastapi import FastAPI
from crud import models
from  crud.database import engine
from sqlalchemy.orm import Session
from typing import List
from crud.route import person 
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

# instatiate our app
app = FastAPI()

# Set allowed origins
origins = ["https://stage2.up.railway.app", '*']

# Enable CORS
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


models.Base.metadata.create_all(engine)

app.include_router(person.router)


# running on debug mode
# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=5000)