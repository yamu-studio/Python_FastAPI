from datetime import datetime
from uuid import uuid4

from sqlalchemy import text, Boolean, Column, ForeignKey, Integer, String, Date, DateTime, LargeBinary
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp

from app.database.database import Base


class UserMaster(Base):
    __tablename__ = "user_masters"
    id = Column(Integer, primary_key=True, index=True,
                comment="ID", autoincrement=True)
    email = Column(String(10), nullable=True)
    password = Column(String(10), nullable=True)
    token = Column(String(256), nullable=True)

    created_at = Column(Timestamp, nullable=True)
    latest_login_at = Column(Timestamp, nullable=True)

    user_id = Column(Integer, ForeignKey("user_masters.id"))


class UserAuth(Base):
    __tablename__ = "youtube_channel_auths"
    id = Column(Integer, primary_key=True, index=True,
                comment="ID", autoincrement=True)
    email = Column(String(10))
    password = Column(String(10))
    token = Column(String(10))

    created_at = Column(Timestamp, nullable=True)
    latest_login_at = Column(Timestamp, nullable=True)

    channel_id = Column(Integer)


class ChannelMaster(Base):
    __tablename__ = "channel_masters"
    id = Column(Integer,  primary_key=True, index=True,
                comment="ID", autoincrement=True)
    created_at = Column(Timestamp, nullable=True)
    is_deleted = Column(Boolean, nullable=True)

    user_id = Column(Integer)
    channel_info_id = Column(Integer, ForeignKey('channel_infos.id'))
    channel_insight_id = Column(Integer, ForeignKey('channel_insights.id'))

    info = relationship("ChannelInfo", foreign_keys=[channel_info_id])
    insight = relationship("ChannelInsight", foreign_keys=[channel_insight_id])


class ChannelInfo(Base):
    __tablename__ = "channel_infos"
    id = Column(Integer, primary_key=True, index=True,
                comment="ID", autoincrement=True)
    channel_name = Column(String(10), nullable=True)
    name = Column(String(10), nullable=True)
    description = Column(String(10), nullable=True)
    janru_cd = Column(Integer)
    thumbnail_path = Column(String(10), nullable=True)
    back_img_path = Column(String(10), nullable=True)
    recent_movie_janru_cds = Column(String(999), nullable=True)
    created_at = Column(Timestamp, nullable=True)
    updated_at = Column(Timestamp, nullable=True)

    # channel_id = Column(Integer, ForeignKey("channel_masters.id"))


class ChannelInsight(Base):
    # class ChannelInsight(InsightBase):
    __tablename__ = "channel_insights"

    id = Column(Integer, primary_key=True, index=True,
                comment="ID", autoincrement=True)
    view_count = Column(Integer)
    favorite_count = Column(Integer)
    comment_count = Column(Integer)
    movie_count = Column(Integer)
    subscriber_count = Column(Integer)

    # created_at = Column(DateTime, nullable=True)
    # updated_at = Column(DateTime, nullable=True)

    # channel_id = Column(Integer, ForeignKey("channel_masters.id"))


class SubscribeChannel(Base):
    __tablename__ = "subscribe_channels"
    id = Column(Integer, primary_key=True, index=True,
                comment="ID", autoincrement=True)
    movie_id = Column(Integer, ForeignKey("movie_masters.id"))
    channel_id = Column(Integer, ForeignKey("channel_masters.id"))

    created_at = Column(Timestamp, nullable=True)

    movie = relationship("MovieMaster", foreign_keys=[
        movie_id])
    channel = relationship("ChannelMaster", foreign_keys=[
        channel_id])


class MovieMaster(Base):
    __tablename__ = "movie_masters"
    id = Column(Integer, primary_key=True, index=True,
                comment="ID", autoincrement=True)
    movie_id = Column(String(3), nullable=True)
    created_at = Column(Timestamp, nullable=True)
    is_deleted = Column(Boolean, nullable=True)

    channel_id = Column(Integer, ForeignKey("channel_masters.id"))
    movie_info_id = Column(Integer, ForeignKey('movie_infos.id'))
    movie_insight_id = Column(Integer, ForeignKey('movie_insights.id'))

    channel = relationship("ChannelMaster", foreign_keys=[
        channel_id])
    info = relationship("MovieInfo", foreign_keys=[
                        movie_info_id])
    insight = relationship("MovieInsight", foreign_keys=[
        movie_insight_id])


class MovieInfo(Base):
    __tablename__ = "movie_infos"
    # __table_args__ = {"comment": "動画情報"}

    id = Column(Integer, primary_key=True, index=True,
                comment="ID", autoincrement=True)
    title = Column(String(10), nullable=True, comment="タイトル")
    description = Column(String(10), nullable=True, comment="概要欄")
    movie_path = Column(String(10), nullable=True)
    thumbnail_path = Column(String(10), nullable=True)
    janru_cd = Column(Integer, nullable=True, comment="ジャンルCD")
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

    movie_id = Column(Integer, ForeignKey("movie_masters.id"), comment="動画ID")
    # movie_id = Column(Integer)


class MovieInsight(Base):
    __tablename__ = "movie_insights"
    __table_args__ = {"comment": "動画情報"}

    id = Column(Integer, primary_key=True, index=True,
                comment="ID", autoincrement=True)

    view_count = Column(Integer)
    favorite_count = Column(Integer)
    comment_count = Column(Integer)
    good_count = Column(Integer)
    bad_count = Column(Integer)

    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

    movie_id = Column(Integer, ForeignKey("movie_masters.id"), comment="動画ID")
    # movie_id = Column(Integer)


class MovieHistory(Base):
    __tablename__ = "movie_histories"
    __table_args__ = {"comment": "動画情報"}

    id = Column(Integer, primary_key=True, index=True,
                comment="ID", autoincrement=True)

    view_second = Column(Integer)
    ip_address = Column(String(10))
    created_at = Column(DateTime, nullable=True)
    latest_viewed_at = Column(DateTime, nullable=True)

    movie_id = Column(Integer, ForeignKey("movie_masters.id"))
    channel_id = Column(Integer, ForeignKey("channel_masters.id"))

    movie = relationship("MovieMaster", foreign_keys=[
        movie_id])
