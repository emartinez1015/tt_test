
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

@router.post("/projects/{project_id}/tasks/", tags=["tasks"])
def create_task(project_id: int):
    return {"message": f"Task created for project {project_id}"}

@router.get("/projects/{project_id}/tasks/", tags=["tasks"])
def read_tasks_for_project(project_id: int):
    return {"message": f"List of tasks for project {project_id}"}


@router.put("/tasks/{task_id}", tags=["tasks"])
def update_task(task_id: int):
    return {"message": f"Task {task_id} updated"}

@router.delete("/tasks/{task_id}", tags=["tasks"])
def delete_task(task_id: int):
    return {"message": f"Task {task_id} deleted"}
