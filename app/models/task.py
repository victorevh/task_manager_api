from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = (Column(String, nullable=False))
    description = (Column(String))

    status = Column(String, default='pending')

    project_id = Column(Integer, ForeignKey('projects.id'))
    assigned_to = Column(Integer, ForeignKey('users.id'))

    project = relationship('Project')
    user = relationship('User')