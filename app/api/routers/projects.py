from fastapi import APIRouter

router = APIRouter()



@router.get("/", tags=["projects"])
def read_projects():
    return {"message": "List of projects"}

@router.post("/projects/", tags=["projects"])
def create_project():
    return {"message": "Project created"}

@router.patch("/projects/{project_id}", tags=["projects"])
def update_project(project_id: int):
    return {"message": f"Project {project_id} updated"}

@router.delete("/projects/{project_id}", tags=["projects"])
def delete_project(project_id: int):
    return {"message": f"Project {project_id} deleted"}
