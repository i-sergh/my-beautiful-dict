from sqlalchemy import Column, Integer, String, TIMESTAMP
from dbengine import Base


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username =Column(String)
    role = Column(String)
    created_at = Column(TIMESTAMP)
    
