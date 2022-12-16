import time
from fastapi import APIRouter, Response, Header, Cookie
from typing import List, Optional
from ..custom_log import log

router = APIRouter(
    tags=["Product"]
)

products = ["Watch", "Camera", "Phone"]


async def time_consuming_functionality():
    time.sleep(4)
    return "Ok"
# belirtilen apinin bekletilmesi icin kullanilabilir fonksiyon


@router.post("/new_product")
def create_product(name: str):
    products.append(name)
    return products


@router.get("/products")
# def get_all_producst():
#     log("Something", "Like sO So")
# burda bulunan logging request calistirildiginda tanimlanan custom_log.log() komutunun calistirdigi fonkssiyonu olusturur
#     return ",".join(products)


async def get_all_products():
    await time_consuming_functionality()
    # fonksiyon da bekletme/yavaslatma icin tanimlanan fonksiyonun tanimlanma sekli
    data = ",".join(products)
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key="Cookie_Input", value="cookie_value_output")
    return response
    # sadece return komutu ile 'product' listesini dondurmek yerine
    # 'media_type'... gibi parametreleri belirlemek icin 'Response' kullanilabilir


@router.get("/headers")
def get_headers(
        response: Response,
        Custom_Header: Optional[List[str]] = Header(None),
        # bilgi iletimi icin kullanilir header olarak belirtilen baslik bir bilgi cikisini temsil eder
        # custom-header olmadan bilgi cikisi olmaz
        Cookie_Input: Optional[str] = Cookie(None),
        # 'Cookie' degerini üst tarafda 'response.set_cookie' icinde tanimladigimiz 'key' degerinden (Cookie_Input) aliyor
        # 'Optional[List]' kullanicidan listelenebiir degerler alir
        # '=' seklinde tanimlama gerektirir(Query,Header,Path...)
):
    if Custom_Header:
        response.headers["custom_response_header"] = ",".join(Custom_Header)
    # 'custom header'i 'custom_response_header' olarak isimlendirdir
    return {
        "Data": products,
        "Cookie": Cookie_Input,
        "Custom_Header": Custom_Header,
    }














































