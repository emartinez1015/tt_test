
from sqlalchemy import Column, String, Text, DateTime, Integer
from app.db.session import Base, engine

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False)
