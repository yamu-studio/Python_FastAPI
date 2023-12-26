from fastapi import FastAPI, HTTPException, Request, status

from fastapi import Depends, APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from pydantic import Json

from app.database.database import get_db
from app.schemas import youtube as y_schemas
from app.cruds import youtube as y_crud

router = APIRouter()


# @router.get("/channels/", response_model=list[y_schemas.Channel])
# def get_channels(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     channels = y_crud.get_channels(db, skip=skip, limit=limit)
#     return channels


# @router.get("/channels/{channel_id}", response_model=y_schemas.Channel)
# def get_channel(channel_id: str, db: Session = Depends(get_db)):
#     channel = y_crud.get_channel(db, channel_id=channel_id)
#     return channel
@router.get("/channels/{channel_id}")
# @router.get("/channels/{channel_id}", response_model=y_schemas.Channel)
def get_movie(channel_id: str, db: Session = Depends(get_db)):
    try:
        channel = y_crud.get_channel(db, channel_id=channel_id)
        print(channel)
        return {
            "master": channel[0],
            "info": channel[1],
            "insight": channel[2]
        }
    except Exception:
        raise HTTPException(status_code=404, detail="movie not found")


@router.get("/movies/")
def get_movies(janru_cd: int = -1, skip: int = -1, limit: int = 100, db: Session = Depends(get_db)):
    movies = y_crud.get_movies(db, janru_cd=janru_cd, skip=skip, limit=limit)
    if not movies:
        raise HTTPException(status_code=404, detail="Video not found")
    else:
        res_val = []
        for movie in movies:
            val = {
                "master": movie[0],
                "info": movie[1],
                "insight": movie[2]
            }
            res_val.append(val)

    return {"list": res_val}


@router.get("/movies/{movie_id}", response_model=y_schemas.MovieMaster)
def get_movie(movie_id: str, db: Session = Depends(get_db)):
    try:
        movie = y_crud.get_movie(db, movie_id=movie_id)
        # channel = y_crud.get_channel(db, channel_id=movie[0].channel_id)
        # print(movie)
        # print(movie.info)
        # print(movie.insight)
        # print(channel)
        # return {
        #     "master": movie[0],
        #     "info": movie[1],
        #     "insight": movie[2],
        #     # "channel": {
        #     #     "master": channel[0],
        #     #     "info": channel[1],
        #     #     "insight": channel[2],
        #     # }
        # }
        # aa = y_schemas.MovieInfos
        # aa.master = movie[0]
        # aa.info = movie[1]
        # return {"title": 1}
        return movie

    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail="movie not found")
    # except MultipleResultsFound:  # type: ignore
    #     raise HTTPException(
    #         status_code=500, detail="Multiple videos found with the same ID")


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
