from fastapi import FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from .database.database import SessionLocal
from .routers import youtube


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


# 404エラーを拾う


@app.exception_handler(404)
def not_found(req: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(content={"notFound": str(req.url)}, status_code=404)


@app.exception_handler(RequestValidationError)
async def handler(request: Request, exc: RequestValidationError):
    print(exc)
    return JSONResponse(content={}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

# 各エンドポイントはここで入れる
app.include_router(youtube.router)
