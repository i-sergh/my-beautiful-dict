from sqlalchemy import Column, Integer, String, TIMESTAMP
from dbengine import Base


class Users(Base):
    __tablename__ = 'users'
    Column('id', Integer)
    Column('name', String)
    Column('role', String)
    Column('created_at', TIMESTAMP)
    
