from datetime import datetime
from uuid import uuid4

from sqlalchemy import text,Boolean, Column, ForeignKey, Integer, String, Date,DateTime,LargeBinary
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp

from .database import Base

# レコードの作成日時と更新日時を定義する。各モデルに継承する。
class TimestampMixin(object):
    created_at = Column(
        Timestamp,
        nullable=False,
        server_default=text("current_timestamp"),
        comment="作成日時",
    )
    updated_at = Column(
        Timestamp,
        nullable=False,
        server_default=text("current_timestamp on update current_timestamp"),
        comment="更新日時",
    )

# ここの構造は、
# ↑末端クラス・テーブル
# ↓期間クラス・テーブル

class Channnel(Base,TimestampMixin):
    __tablename__ = "channels"
    __table_args__ = {"comment": "チャンネル情報"}

    id = Column(Integer, primary_key=True, index=True,comment="ID")
    channel_id = Column(String(32), nullable=False, comment="チャンネルID")
    name = Column(String(50), nullable=False, comment="チャンネル名")
    description = Column(String(3000), nullable=False, comment="自己紹介")

    # user = relationship("User", back_populates="channel", uselist=False)
    # user_id = Column(String(32), ForeignKey("user.user_id"))
    # movie = relationship("Movie", back_populates="channel")

class Movie(Base,TimestampMixin):
    __tablename__ = "movies"
    __table_args__ = {"comment": "動画情報"}

    id = Column(Integer, primary_key=True, index=True,comment="ID", autoincrement=True)
    movie_id = Column(String(32), nullable=True, comment="動画ID")
    title = Column(String(50), nullable=True, comment="タイトル")
    description = Column(String(3000), nullable=True, comment="概要欄")
    src = Column(LargeBinary, nullable=True, comment="動画")
    thumbnail = Column(LargeBinary, nullable=True)
    channel_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

    # channel_id = Column(Integer, ForeignKey("channels.channel_id"))

    # channel = relationship("Channnel", back_populates="movie")


class User(Base,TimestampMixin):
    __tablename__ = "users"
    __table_args__ = {"comment": "ユーザー情報"}

    id = Column(Integer, primary_key=True, index=True,comment="ID")
    user_id = Column(String(32), nullable=False, comment="ユーザーID")
    name = Column(String(50), nullable=False, comment="名前")
    birth_date = Column(Date, nullable=True, comment="生年月日")
    channel_id = Column(String(32), ForeignKey("channel.channel_id"))

    # contact = relationship("Contact", back_populates="profile", uselist=False)
    # channel = relationship("Channel", back_populates="user", uselist=False)
