from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import DB_USER,PASSWORD,HOST,DATABASE,PORT

print(DB_USER)
user = DB_USER
password = PASSWORD
host = HOST
port = PORT
db_name = DATABASE


# engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db_name}')

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()