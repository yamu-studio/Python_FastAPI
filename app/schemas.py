from datetime import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
  id:int
  user_id: str
  name: str
  birth_date: datetime
  created_at: datetime
  updated_at: datetime

class ChannelBase(BaseModel):
  id:int
  channel_id: str
  name: str
  description: str

  # user_id: str
  created_at: datetime
  updated_at: datetime

class MovieBase(BaseModel):
  id:int
  movie_id: str
  title: str
  description: str
  src: object

  # channel_id: str
  # created_at: datetime
  # updated_at: datetime
class MovieCreate(MovieBase):
  pass


class UserCreate(UserBase):
  pass


class User(UserBase):
  id: int

  class Config:
    orm_mode = True

class Channel(ChannelBase):
  id: int

  class Config:
    orm_mode = True

class Movie(MovieBase):
  id: int
  
  class Config:
    orm_mode = True