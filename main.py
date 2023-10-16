import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from db import db
from api.v1 import service


load_dotenv()


app = FastAPI(
    title='Pick',
    description='Pick',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json'
)


@app.on_event('startup')
async def on_startup():
    engine = create_async_engine(os.environ.get('POSTGRES_DSN'),
                                 echo=False, future=True)
    db.async_session = sessionmaker(engine, class_=AsyncSession,
                                    expire_on_commit=False)
    async with engine.begin() as conn:
        await conn.run_sync(db.Base.metadata.drop_all)
        await conn.run_sync(db.Base.metadata.create_all)


@app.on_event('shutdown')
async def on_shutdown():
    db.async_session.close_all()


app.include_router(service.router, prefix='')


if __name__ == "__main__":
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8080,
        reload=True
    )
