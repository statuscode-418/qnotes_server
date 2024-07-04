from fastapi import FastAPI
from . import models
from .database import engine
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .routers import user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(
            host= 'ep-fragrant-mouse-a1rwbv9e.ap-southeast-1.aws.neon.tech',
            database='neondb',
            user='neondb_owner',
            password='gKo5tSFXnfY0',
            cursor_factory=RealDictCursor,
            sslmode='require', # check for secure connection
            )
        cursor = conn.cursor()
        print('database connection established')
        break
    except Exception as error:
        print('Database not connected ', error)
        time.sleep(2)



app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Hello Jonogons"}