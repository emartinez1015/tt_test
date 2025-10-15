import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app.db.base import Base

class Project(Base):
    __tablename__ = "projects"

    id = sa.Column(sa.Integer, primary_key=True, index=True, autoincrement=True)
    name = sa.Column(sa.String(255), nullable=False)
    description = sa.Column(sa.Text, nullable=True)
    created_at = sa.Column(sa.DateTime, server_default=sa.text("now()"), nullable=False)

    tasks = relationship("Task", back_populates="project")
