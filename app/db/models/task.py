from sqlalchemy import Column, String, Integer, Boolean, Date, ForeignKey
from app.db.session import Base, engine



class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    title = Column(String, nullable=False)
    priority = Column(Integer, nullable=False)
    completed = Column(Boolean, default=False)
    due_date = Column(Date, nullable=True)

