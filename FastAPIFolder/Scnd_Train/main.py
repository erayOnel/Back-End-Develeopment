from . import models
from fastapi import FastAPI, Request
from .Routers import blog, user, article, product, file
from . import authentication, dependencies
from.database import engine
from .teapot import StoryException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from .templates import templates
import time


#dosyalari browserdan static olarak erisilebilir kilmak icin ihtiyacimiz olan 'import'


app = FastAPI()


app.include_router(dependencies.router)
app.include_router(templates.router)
app.include_router(file.router)
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(status_code=418, content={
        "detail": exc.name
    })

# buradaki 'exception_handler','db_article' icerisinde bulunan 'StoryException' fonksiyonuna donuyor


models.db_User.metadata.create_all(engine)


@app.middleware("http")
async def add_middleware(request: Request, call_next):
    #  'call_next' path olarak request degerini referans alir ve ona return eder
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    response.headers["duration"] = str(duration)
    return response
    # 'middleware' butun 'api'ler(request'ler) icin networkde tanimlamalar yapmaya yarar


app.mount("/Files", StaticFiles(directory="C:/Users/erayo/PycharmProjects/pythonProject/FastAPIFolder/Scnd_Train/Files"), name="Files")
# 'app.mount' icinde belirtilen ilk parametre(/Files) üzerinden ulasilacak 'url'i belirtir,'directory' parametresi alinacak itemlerin bulundugu dosyayi
app.mount("/templates/static",
          StaticFiles(directory="C:/Users/erayo/PycharmProjects/pythonProject/FastAPIFolder/Scnd_Train/templates/static"),
          name="try"
          )


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.0", port=8000)












