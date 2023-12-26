from fastapi import Depends, APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
import io
import base64
from pydantic import Json

from ..database.database import get_db
from ..schemas import youtube as y_schemas
from ..cruds import youtube as y_crud

router = APIRouter()


@router.get("/channels/", response_model=list[y_schemas.Channel])
def get_channels(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    channels = y_crud.get_channels(db, skip=skip, limit=limit)
    return channels


@router.get("/channels/{channel_id}", response_model=y_schemas.Channel)
def get_channel(channel_id: str, db: Session = Depends(get_db)):
    channel = y_crud.get_channel(db, channel_id=channel_id)
    return channel


@router.get("/movies/", response_model=list[y_schemas.Movie])
def get_movies(janru_cd: int = 0, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = y_crud.get_movies(db, janru_cd=janru_cd, skip=skip, limit=limit)
    return movies


@router.get("/movies/{movie_id}", response_model=y_schemas.Movie)
def get_movie(movie_id: str, db: Session = Depends(get_db)):
    movie = y_crud.get_movie(db, movie_id=movie_id)
    # print(movie.)
    return movie


@router.get("/movies/{movie_id}/src", response_model=y_schemas.MovieSrc)
def get_movie_src(movie_id: str, db: Session = Depends(get_db)):
    movie = y_crud.get_movie(db, movie_id=movie_id)
    return StreamingResponse(io.BytesIO(movie.src), media_type="video/mp4")


@router.get("/movies/{movie_id}/insight", response_model=y_schemas.MovieInsight)
def get_movie_insight(movie_id: int, db: Session = Depends(get_db)):
    movie = y_crud.get_movie_insight(db, movie_id=movie_id)
    return movie


@router.post("/movie/upload", response_model=y_schemas.Movie)
async def upload_file(movie: Json = Form(), file: UploadFile = File(...), db: Session = Depends(get_db)):
    # 一旦読み込み必要
    movieFile = await file.read()
    # base64 を使うならこんな感じ
    # bin_data: bytes = base64.b64encode(movieFile).decode()

    res_movie = y_crud.create_movie(db, movie, movieFile)
    return res_movie


# ●分割アップロードの流れ
# ・フロント側でblobにし、それを何個かに分割する(dataとindex(何番目か))
# ・大元をインサート(Update)する→動画情報とindex(何個あるか)
# ・非同期で分割したやつを入れる(別テーブルとしてか大元テーブルにmovie_packet_1のようにして入れるか)
# →ほかにも方法探してみよ
