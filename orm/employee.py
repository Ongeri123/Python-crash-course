
from db import PG
import pygame as pg

class Employee():

    def __init__(self):
        pg=PG()
        self.pg=pg
        query="""
            CREATE TABLE IF NOT EXISTS employee(
              id BIGSERIAL PRIMARY KEY,
              name TEXT NOT NULL,
              email TEXT NOT NULL UNIQUE
            )
        """
        pg.pg_query(query=query)
#add 
    def add(self,name,email):
        pg=PG()
        query="""
            INSERT INTO employee
            (name,email)
            VALUES
            (%s,%s)
            """
        pg.pg_query(query=query,params=(name,email))

    def all(self):
        pg = PG()
        query = """
        SELECT * FROM employee
        """
        return pg.pg_query(query=query)

emp1=Employee()
#emp1.add(name='Joan',email='joan@gmail.com')
#emp1.add(name='Kev',email='kev@gmail.com')

# k="""
# ALTER TABLE employee
# ADD COLUMN age INTEGER
# """

