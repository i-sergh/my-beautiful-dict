from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy import MetaData

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

DB_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocmmit=False, autoflush=False, bind=engine)

Base: DeclarativeMeta = declarative_base()

