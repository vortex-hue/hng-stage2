from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Person(Base):
    __tablename__ = "person"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    age = Column(String)




