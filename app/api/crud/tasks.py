from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.task import Task

async def get_task(db: AsyncSession, task_id: str):
    result = await db.execute(select(Task).where(Task.id == task_id))
    return result.scalar_one_or_none()

async def get_tasks_by_project(db: AsyncSession, project_id: str, limit=50, offset=0):
    result = await db.execute(
        select(Task)
        .where(Task.project_id == project_id)
        .order_by(Task.priority.desc())
        .limit(limit)
        .offset(offset)
    )
    return result.scalars().all()

async def create_task(db: AsyncSession, obj_in, project_id: str):
    task = Task(**obj_in.dict(), project_id=project_id)
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task

async def update_task(db: AsyncSession, db_obj: Task, obj_in):
    for field, value in obj_in.dict(exclude_unset=True).items():
        setattr(db_obj, field, value)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj

async def delete_task(db: AsyncSession, db_obj: Task):
    await db.delete(db_obj)
    await db.commit()
