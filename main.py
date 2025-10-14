from fastapi import FastAPI


from app.api.routers import projects, tasks
from app.db.session import Base, engine


Base.metadata.create_all(engine)

app = FastAPI(debug=True)



@app.get("/")
def read_root():
    return "Projects API"

app.include_router(projects.router, prefix="/projects", tags=["projects"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
