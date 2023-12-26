from datetime import datetime
from fastapi import File, UploadFile
from pydantic import BaseModel
import json


class UserBase(BaseModel):
    id: int
    user_id: str
    name: str
    birth_date: datetime
    created_at: datetime
    updated_at: datetime


class ChannelBase(BaseModel):
    id: int
    channel_id: str
    name: str
    description: str

    # user_id: str
    created_at: datetime
    updated_at: datetime


class MovieBase(BaseModel):
    id: int
    movie_id: str
    title: str
    description: str


class MovieCreate(MovieBase):
    src: UploadFile = File(...)
    pass


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        # ↓使えないらしい？
        # orm_mode = True
        from_attributes = True


class Channel(ChannelBase):
    id: int

    class Config:
        from_attributes = True


class MovieSrc(MovieBase):
    src: bytes


class Movie(MovieBase):
    id: int
    movie_id: str
    title: str
    description: str

    channel_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class MovieInsight(BaseModel):
    view_count: int
    good_count: int
    bad_count: int
    comment_count: int
