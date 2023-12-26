from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.user_id == user_id).first()


# def get_user_by_name(db: Session, name: str):
#     return db.query(models.User).filter(models.User.name == name).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     new_user = models.User(**user.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

def get_channel(db: Session, channel_id: str):
    return db.query(models.Channnel).filter(models.Channnel.channel_id == channel_id).first()


def get_channels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Channnel).offset(skip).limit(limit).all()

def create_movie(db: Session, movie: schemas.MovieCreate):
    new_movie = models.Movie(**movie.dict())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie