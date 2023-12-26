from fastapi import Depends, FastAPI, HTTPException,Request,File, UploadFile,status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError



from sqlalchemy.orm import Session

from . import crud, models, schemas
# from .database import SessionLocal, engine

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
  "http://localhost:3000",
  "http://localhost"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)


def get_db():
  db = SessionLocal()
  try:
      yield db
  finally:
      db.close()

# 404エラーを拾う
@app.exception_handler(404)
def not_found(req: Request, exc: HTTPException) -> JSONResponse:
  return JSONResponse(content={"notFound": str(req.url)}, status_code=404)

@app.exception_handler(RequestValidationError)
async def handler(request:Request, exc:RequestValidationError):
    print(exc)
    return JSONResponse(content={}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


@app.get("/") 
def hello_world(): 
  return {"message":"Hello world"}



# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_name(db, name=user.name)
#     if db_user:
#         raise HTTPException(status_code=400, detail=f"User name: {user.name} already exists.")
#     return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  users = crud.get_users(db, skip=skip, limit=limit)
  return users

@app.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id:str, db: Session = Depends(get_db)):
  user = crud.get_user(db, user_id=user_id)
  return user

# @app.get("/createUser/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate,db: Session = Depends(get_db)):
#     users = crud.create_user(db, user=user)
#     return users

@app.get("/channels/", response_model=list[schemas.Channel])
def get_channels(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  channels = crud.get_channels(db, skip=skip, limit=limit)
  return channels

@app.get("/channels/{channel_id}", response_model=schemas.Channel)
def get_channel(channel_id:str, db: Session = Depends(get_db)):
  channel = crud.get_channel(db, channel_id=channel_id)
  return channel

@app.post("/test/upload", response_model=schemas.Movie)
# async def upload_file(movie: schemas.MovieCreate,file: UploadFile = File(...),db: Session = Depends(get_db)):
async def upload_file(movie: schemas.MovieCreate,db: Session = Depends(get_db)):
  # やること
  # ・持ってきたfileをblob型へ？
  # ・直接行けるか
  # movie.channel_id = "asdfgh"
  # movie.src=file.file
  # return {'filename': file.filename}
  movie = crud.create_movie(db,movie)
  return movie


# ●分割アップロードの流れ
# ・フロント側でblobにし、それを何個かに分割する(dataとindex(何番目か))
# ・大元をインサート(Update)する→動画情報とindex(何個あるか)
# ・非同期で分割したやつを入れる(別テーブルとしてか大元テーブルにmovie_packet_1のようにして入れるか)