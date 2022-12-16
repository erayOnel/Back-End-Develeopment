from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from ..schemas import ProductSchema
from ..custom_log import log
from fastapi.background import BackgroundTasks

router = APIRouter(
    tags=["Templates"],
    prefix="/templates"
)


templates = Jinja2Templates(directory="C:/Users/erayo/PycharmProjects/pythonProject/FastAPIFolder/Scnd_Train/templates")
# 'template'in bulundugu dosyaya yonlendirmek icin bulunan


@router.post("/products/{id}")
def get_product(id: int,
                product: ProductSchema,
                request: Request,
                bt: BackgroundTasks
                ):
    bt.add_task(log_template_call, f"wth {id}")
    # 'BackgroundTasks' request islemi tamamlandiktan sonra calismaya devam eden fonksiyonlari tanimlamaya yarar
    return templates.TemplateResponse(
        "product.html",
        {
            "request": request,
            "id": id,
            "title": product.Title,
            "description": product.Description,
            "price": product.Price
        }
    )


def log_template_call(message: str):
    log("MyAPI", message)



