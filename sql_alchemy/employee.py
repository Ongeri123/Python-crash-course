from typing import List
from sqlalchemy import String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column ,Session

from engine import engine

class Base(DeclarativeBase):
    pass

class Employee(Base):
    __tablename__="employee"

    #columns
    id: Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    name:Mapped[str]=mapped_column(Text,nullable=False)
    email:Mapped[str]=mapped_column(Text, nullable=False, unique=True)

#create table if it doesnt exist
Base.metadata.create_all(engine) 

with Session(engine) as session:
    name = "Jacob"
    email ="jacob@gmail.com"


    
    # #create data
    # emp=Employee(name=name,email=email)
    # session.add(emp)
    # session.commit()