from sqlalchemy.orm import Session
import base64
import datetime

from ..models import youtube as y_model
from ..schemas import youtube as y_schema


def get_user(db: Session, user_id: str):
    return db.query(y_model.User).filter(y_model.User.user_id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(y_model.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: y_schema.UserCreate):
    new_user = y_model.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_channels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(y_model.Channnel).offset(skip).limit(limit).all()


def get_channel(db: Session, channel_id: str):
    return db.query(y_model.Channnel).filter(y_model.Channnel.channel_id == channel_id).first()


def get_movies(db: Session, janru_cd: int = 0, skip: int = 0, limit: int = 100):
    if (janru_cd == 0):
        return db.query(y_model.Movie).offset(skip).limit(limit).all()
    else:
        return db.query(y_model.Movie).filter(y_model.Movie.janru_cd == janru_cd).offset(skip).limit(limit).all()


def get_movie(db: Session, movie_id: str):
    return db.query(y_model.Movie).filter(y_model.Movie.movie_id == movie_id).first()


def get_movie_insight(db: Session, movie_id: int):
    return db.query(y_model.MovieInsight).filter(y_model.MovieInsight.movie_id == movie_id).first()


def create_movie(db: Session, movie, file):
    new_movie = y_model.Movie()
    new_movie.movie_id = movie["movie_id"]
    new_movie.title = movie["title"]
    new_movie.description = movie["description"]
    new_movie.channel_id = movie["channel_id"]
    new_movie.created_at = datetime.datetime.now()
    new_movie.updated_at = datetime.datetime.now()
    new_movie.src = file

    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie
