import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app.db.base import Base

class Task(Base):
    __tablename__ = "tasks"

    id = sa.Column(sa.Integer, primary_key=True, index=True, autoincrement=True)
    title = sa.Column(sa.String(255), nullable=False)
    description = sa.Column(sa.Text, nullable=True)
    priority = sa.Column(sa.Integer, nullable=True)
    completed = sa.Column(sa.Boolean, default=False)
    created_at = sa.Column(sa.DateTime, server_default=sa.text("now()"), nullable=False)
    project_id = sa.Column(sa.Integer, sa.ForeignKey("projects.id", ondelete="CASCADE"))

    project = relationship("Project", back_populates="tasks")

    __table_args__ = (
        sa.Index("ix_tasks_project_priority", "project_id", "priority"),
    )
