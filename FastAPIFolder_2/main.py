from fastapi import FastAPI
from . import models
from .routers import posts
from .database import engine
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.include_router(posts.router)

models.Base.metadata.create_all(engine)

app.mount("/images", StaticFiles(directory="C:/Users/erayo/PycharmProjects/pythonProject/FastAPIFolder_2/images"), name="images")
origins = [
    "http://localhost:4540"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# 'CORS(Cross-Origin Resource Sharing)' olarak tanimlanan bu kod dizini yazdigimiz back-end odakli kodun front-end yazilimlarla calisabilmesini saglar
