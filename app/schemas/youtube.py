from datetime import datetime
from fastapi import File, UploadFile
from pydantic import BaseModel, Field


class ChannelInfo(BaseModel):
    channel_name: str
    name: str
    description: str
    thumbnail_path: str
    back_img_path: str
    recent_movie_janru_cds: str
    janru_cd: int

    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class ChannelInsight(BaseModel):
    view_count: int
    favorite_count: int
    comment_count: int
    movie_count: int
    subscriber_count: int

    class Config:
        orm_mode = True


class ChannelMaster(BaseModel):
    id: int
    created_at: datetime

    info: ChannelInfo
    insight: ChannelInsight

    class Config:
        orm_mode = True


class MovieInfo(BaseModel):
    title: str
    description: str
    thumbnail_path: str
    movie_path: str
    janru_cd: int

    created_at: datetime
    updated_at: datetime

    class Config:
        # fields = {'movie_id': 'movieID'}  # API 返却名を設定
        orm_mode = True


class MovieInsight(BaseModel):
    view_count: int
    comment_count: int
    good_count: int
    bad_count: int

    class Config:
        orm_mode = True


class MovieMaster(BaseModel):
    id: int
    movieID: str = Field(alias="movie_id")
    time_longth: int
    created_at: datetime

    info: MovieInfo
    insight: MovieInsight
    channel: ChannelMaster

    class Config:
        orm_mode = True


class MovieHistoryRequest(BaseModel):
    movie_id: int
    view_second: int
    channel_id: int
    is_watched: bool = False

    class Config:
        orm_mode = True


class CommentInfo(BaseModel):
    comment: str

    created_at: datetime
    updated_at: datetime

    class Config:
        # fields = {'movie_id': 'movieID'}  # API 返却名を設定
        orm_mode = True


class CommentInsight(BaseModel):
    view_count: int
    good_count: int
    bad_count: int

    class Config:
        orm_mode = True


class CommentMaster(BaseModel):
    id: int
    movieID: int = Field(alias="movie_id")
    # channelID: str = Field(alias="channel_id")
    # replyCommentID: str = Field(alias="reply_comment_id")
    created_at: datetime

    info: CommentInfo
    insight: CommentInsight
    channel: ChannelMaster
    # rep_comment:

    class Config:
        orm_mode = True


class AddCommentRequest(BaseModel):
    comment: str
    movie_id: int
    channel_id: int

    class Config:
        orm_mode = True
