from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import DB_USER, PASSWORD, HOST, PORT, DATABASE

user = DB_USER
password = PASSWORD
host = HOST
port = PORT
db_name = DATABASE


engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
