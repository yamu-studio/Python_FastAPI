from sqlalchemy import desc
from sqlalchemy.orm import Session
import base64
import datetime

from app.models import youtube as y_model


def get_subscribe_channels(db: Session, channel_id: int, limit: int = 100):
    query = db.query(y_model.SubscribeChannel).filter(
        y_model.SubscribeChannel.channel_id == channel_id).limit(limit)
    return query.all()


def get_channel(db: Session, channel_id: int):
    channel = db.query(y_model.ChannelMaster).filter(
        y_model.ChannelMaster.id == channel_id).one()
    return channel


def auth_channel(db: Session, channel_id: int, email: str, passcode: str):
    channel = db.query(y_model.ChannelMaster).filter(
        y_model.ChannelMaster.id == channel_id).one()
    return channel


def get_movies(db: Session, channel_id: int = -1, word: str = "", janru_cd: int = -1,  limit: int = 100):
    query = db.query(y_model.MovieMaster)
    if (-1 < janru_cd):
        query = query.filter(
            y_model.MovieInfo.janru_cd == janru_cd)
    elif (word != ""):
        query = query.filter(
            y_model.MovieInfo.title.contains(word))
    elif (-1 < channel_id):
        query = query.filter(
            y_model.MovieMaster.channel_id == channel_id)
    return query.limit(limit).all()

# 検索機能で別途分けるときはこっちを使う
# def search_movies(db: Session, word: str = "", limit: int = 100):
#     query = db.query(y_model.MovieMaster).filter(
#         y_model.MovieInfo.title.contains(word)).limit(limit)
#     return query.all()


def get_movie(db: Session, movie_id: str):
    movie = db.query(y_model.MovieMaster).filter(
        y_model.MovieMaster.movie_id == movie_id).one()
    return movie


def get_my_history_movies(db: Session, channel_id: int, limit: int = 100):
    query = db.query(y_model.MovieHistory).filter(
        y_model.MovieHistory.channel_id == channel_id).order_by(desc(y_model.MovieHistory.latest_viewed_at))

    return query.limit(limit).all()


def insert_history_movie(db: Session, movie_id: int, view_second: int, channel_id: int, ip_address: str = ""):
    history = y_model.MovieHistory()
    history.movie_id = movie_id
    history.view_second = view_second
    history.channel_id = channel_id
    history.ip_address = ip_address
    history.created_at = datetime.datetime.now()
    history.latest_viewed_at = datetime.datetime.now()
    db.add(history)
    # db.flush()  # 一時的保存(今回はいらない)
    db.commit()
    return history


def update_history_movie(db: Session, history: y_model.MovieHistory, view_second: int, is_watched: bool = False):
    history.view_second = view_second
    if (is_watched):
        history.is_watched = 1
    history.latest_viewed_at = datetime.datetime.now()
    db.commit()
    return history


def get_history_movie(db: Session, channel_id: int, movie_id: int):
    history = db.query(y_model.MovieHistory).filter(
        y_model.MovieHistory.channel_id == channel_id, y_model.MovieHistory.movie_id == movie_id).one()
    return history


def get_comments(db: Session, movie_id: int, limit: int = 100):
    query = db.query(y_model.CommentMaster).filter(
        y_model.CommentMaster.movie_id == movie_id)

    return query.limit(limit).all()


def insert_comment(db: Session, text: str, movie_id: int, channel_id: int):
    comment = y_model.CommentMaster()
    comment_info = y_model.CommentInfo()
    comment_insight = y_model.CommentInsight()

    comment_info.comment = text
    comment_info.updated_at = datetime.datetime.now()
    comment_info.created_at = datetime.datetime.now()
    db.add(comment_info)
    db.flush()  # 一時的保存

    comment_insight.view_count = 0
    comment_insight.good_count = 0
    comment_insight.bad_count = 0
    comment_insight.updated_at = datetime.datetime.now()
    comment_insight.created_at = datetime.datetime.now()
    db.add(comment_insight)
    db.flush()  # 一時的保存

    comment.movie_id = movie_id
    comment.channel_id = channel_id
    comment.comment_info_id = comment_info.id
    comment.comment_insight_id = comment_insight.id
    comment.created_at = datetime.datetime.now()

    db.add(comment)
    # db.flush()  # 一時的保存(今回はいらない)
    db.commit()
    return comment

# 直接動画データをDBに格納するならこうする？(重たくなる)
# def create_movie(db: Session, movie, file):
#     new_movie = y_model.Movie()
#     new_movie.movie_id = movie["movie_id"]
#     new_movie.janru_cd = 1
#     new_movie.title = movie["title"]
#     new_movie.description = movie["description"]
#     new_movie.channel_id = movie["channel_id"]
#     new_movie.created_at = datetime.datetime.now()
#     new_movie.updated_at = datetime.datetime.now()
#     new_movie.src = file
#     db.add(new_movie)
#     db.flush()

#     new_movie_insight = y_model.MovieInsight()
#     new_movie_insight.movie_id = new_movie.id
#     db.add(new_movie_insight)
#     db.commit()
#     db.refresh(new_movie)
#     return new_movie
