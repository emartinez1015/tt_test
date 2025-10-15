from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.project import Project

async def get_project(db: AsyncSession, project_id: str):
    result = await db.execute(select(Project).where(Project.id == project_id))
    return result.scalar_one_or_none()

async def create_project(db: AsyncSession, obj_in):
    project = Project(**obj_in.dict())
    db.add(project)
    await db.commit()
    await db.refresh(project)
    return project

async def update_project(db: AsyncSession, db_obj: Project, obj_in):
    for field, value in obj_in.dict(exclude_unset=True).items():
        setattr(db_obj, field, value)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj

async def delete_project(db: AsyncSession, db_obj: Project):
    await db.delete(db_obj)
    await db.commit()
