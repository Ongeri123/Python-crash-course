from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

db_credentials = {
    "drivername": "postgresql+psycopg",
    "host": "aws-1-ap-southeast-1.pooler.supabase.com",
    "database": "postgres",
    "username": "postgres.umtebhxgvfctvwmfvwnm",
    "password": "#Newtoh13Ongeri",
    "port": "5432",
}

DATABASE_URL=URL.create(**db_credentials)

#create engine
engine=create_engine(DATABASE_URL,echo=True,future=True)

with engine.connect() as conn:
    result=conn.execute(text("SELECT * FROM employee"))
    rows=result.fetchall()

    for row in rows:
        print(row)
