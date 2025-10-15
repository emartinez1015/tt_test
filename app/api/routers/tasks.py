from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.task import TaskOut, TaskUpdate
from app.api.crud import tasks as crud
from app.api.deps import get_db
from app.core.security import verify_api_key

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.put("/{task_id}", response_model=TaskOut, dependencies=[Depends(verify_api_key)])
async def update_task(
    task_id: int,
    payload: TaskUpdate,
    db: AsyncSession = Depends(get_db)
):
    task = await crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    updated_task = await crud.update_task(db, task, payload)
    return updated_task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(verify_api_key)])
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    task = await crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    await crud.delete_task(db, task)
    return None
