from fastapi import FastAPI, HTTPException, Request, status

from fastapi import Depends, APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from pydantic import Json

from app.database.database import get_db
from app.schemas import youtube as y_schemas
from app.cruds import youtube as y_crud

router = APIRouter()


@router.get("/movies/", response_model=list[y_schemas.MovieMaster])
def get_movies(janru_cd: int = -1, limit: int = 100, db: Session = Depends(get_db)):
    movies = y_crud.get_movies(db, janru_cd=janru_cd, limit=limit)
    if not movies:
        raise HTTPException(status_code=404, detail="Movies not found")
    return movies


@router.get("/movies/history")
def get_history_movies(channel_id: int, limit: int = 100, db: Session = Depends(get_db)):
    movies = y_crud.get_my_history_movies(
        db, channel_id=channel_id, limit=limit)
    if not movies:
        raise HTTPException(status_code=401, detail="Movie not found")
    return movies


@router.post("/movies/history/add")
def add_history_movie(history_item: y_schemas.MovieHistoryRequest, db: Session = Depends(get_db)):
    history = None
    try:
        history = y_crud.get_history_movie(
            db, channel_id=history_item.channel_id, movie_id=history_item.movie_id)
        # 対象を更新する
        history = y_crud.update_history_movie(
            db, history=history, view_second=history_item.view_second, is_watched=history_item.is_watched)
    except Exception:
        # 対象を作成する
        history = y_crud.insert_history_movie(
            db, movie_id=history_item.movie_id, view_second=history_item.view_second, channel_id=history_item.channel_id)
    return history


@router.get("/movies/{movie_id}", response_model=y_schemas.MovieMaster)
def get_movie(movie_id: str, db: Session = Depends(get_db)):
    try:
        movie = y_crud.get_movie(db, movie_id=movie_id)
        return movie

    except Exception as e:
        # print(e)
        raise HTTPException(status_code=404, detail="Movie not found")


@router.post("/comments/add")
def add_comment(comment_item: y_schemas.AddCommentRequest, db: Session = Depends(get_db)):
    comment = y_crud.insert_comment(db, text=comment_item.comment,
                                    movie_id=comment_item.movie_id, channel_id=comment_item.channel_id)
    return comment


@router.get("/comments", response_model=list[y_schemas.CommentMaster])
def get_comments(movie_id: int, db: Session = Depends(get_db)):
    comments = y_crud.get_comments(db, movie_id=movie_id)
    if not comments:
        raise HTTPException(status_code=404, detail="Comments not found")
    return comments


# @router.post("/movie/upload")
# # @router.post("/movie/upload", response_model=y_schemas.Movie)
# async def upload_file(movie: Json = Form(), file: UploadFile = File(...), db: Session = Depends(get_db)):
#     # 一旦読み込み必要
#     movieFile = await file.read()
#     # base64 を使うならこんな感じ
#     # bin_data: bytes = base64.b64encode(movieFile).decode()

#     res_movie = y_crud.create_movie(db, movie, movieFile)
#     return res_movie


# ●分割アップロードの流れ
# ・フロント側でblobにし、それを何個かに分割する(dataとindex(何番目か))
# ・大元をインサート(Update)する→動画情報とindex(何個あるか)
# ・非同期で分割したやつを入れる(別テーブルとしてか大元テーブルにmovie_packet_1のようにして入れるか)
# →ほかにも方法探してみよ
