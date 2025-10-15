from fastapi import FastAPI
from app.api.routers import projects, tasks
from app.db.session import engine
from app.db.base import Base

app = FastAPI(title="Projects & Tasks API")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(projects.router)
app.include_router(tasks.router)
