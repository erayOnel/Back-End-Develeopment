from fastapi import APIRouter,status,HTTPException,Response,Query,Body,Path,Depends
from enum import Enum
from pydantic import BaseModel
from typing import Optional,List
from ..custom_log import log


router=APIRouter(
    prefix="/blog",
    tags=["Blog"],
    dependencies=[Depends(log)],
)


def req_param():
    return {"Message": "FastAPI learning is funnier than the Flask btw"}


@router.get("/",
            summary="Retrieve all blogs",
            description="This api call simulates fetching all blogs",
            response_description="List of all (avaliable) blogs", status_code=status.HTTP_200_OK)
#'summary' ozet (default hali fonksiyonun isminin biraz duzenlenmis halidir) , 'description' biraz daha ayrintili aciklamalar ekler
#'respone_description' ise swaggerda bulunan response(description)bolumune acikma ekler
def page(page_size=10,page=4,req_param:dict=Depends(req_param)):
    return {"Message":f"Those all {page_size} blogs are on the {page} page parameter is {req_param}"}
    #default degerler fonksiyon icinde tanimli


@router.get("/{id}",status_code=status.HTTP_200_OK)
def give_with_id(id:int):
    return {"Message":f"That's the blog with {id} id "}
    #dinamik 'url'ler  ayni ust linki paylasan baska bir url varsa o fonksiyona takilabilir


@router.get("/{id}/comments/{comment_id}",status_code=status.HTTP_200_OK)
def get_specific_comment(blog_id:int,comment_id:int,username:str):
    """
    I was lost
    **Raise**
    **the Flag**
    """
    #yukarda belirtilen semboller swagger tarafindan (default) tanimlanmistir
    return {f"Comment":f"Comment with {comment_id} id for blog {blog_id} id from username : {username} "}


class Blog_Type(str, Enum):
    a = "accept"
    b = "bool"
    c = "certain"


@router.get("/type/{type}")
def get_blog_type(type: Blog_Type):
    #rotation icinde belirtilen dinamik url fonksiyona  tasinmistir
    return {"Message":f"Blog type is {type}"}


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_specific_blog(id: int, response: Response):
    if id > 5:
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"This blog with {id} id doesn't exists")
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Message": f"There is no blog with {id} id"}
        #kendi return degerimizi dondurmek icin response modelini kullanabiliriz
    else:
        return {"Message": f"That's the blog with {id} id"}


class BlogScheme(BaseModel):
    Title: str
    Body: str
    Comment: str
    Published: Optional[bool]
    #'BaseModel' , 'Request body' icin olusturdugumuz semadir


@router.post("/new/{id}/blog", status_code=status.HTTP_201_CREATED)
def create_blog(blog: BlogScheme, id: int, version: int):
    return {
        "Id": id,
        "Version": version,
        "Blog_Data": blog,
}
#'id','version','blog('BlogScheme'dan referans alinan)' birlikte belirtilebilir parametrelerdir


@router.post("/new/{id}/comment/{comment_id}")
def create_comment(blog: BlogScheme, id: int,comment_title: int=Query(None,
                                                               title="Id of the comment",
                                                               description="Some description for comment_id",
                                                               alias="Comment_Id",
                                                               deprecated=False
                                                               ),
                   content:str=Body("There is a body",min_length=4,max_length=16),
                   version:Optional[List[str]]=Query(None,alias="Version"),
                   comment_id:int=Path(None,lt=20,gt=2)
                   #version_2:Optional[List[str]]=Query(["1.5","7.5","6"])
                   #content_2:str=Body(Ellipsis),
                   ):
    # 'comment_id' le,lt,gt,ge(less than,less that or equal to,greater than...) gibi degerler icerir
    # 'version_2':liste elemanlarini default olarak tanimlamaya yarar
    # (degistirilebilir,kaldırilabilir,yenisi eklenebilir)
    # 'regex' parametresi 'Body'nin bulundugu degisken icin(content)tanimlanan karakterleri tnimlar
    # 'content(1)':opsiyonel girdidir yani request icin doldurulmasi sart degil,response icerisinde(default haliyle),)gorunur
    # 'content_2(...)':request icerisinde bulunmak zorundadir(Ellipsis olarak da bilinir)
    # 'query' url sonunda (? isaretinden sonra gelen) belirtilen parametrelerdir
    # 'alias' swaggerda bulunan girdinin hitabetini ve url degiskenini düzenler
    # "deprecated" girdinin kullanimdan kaldirildigini/kaldirilmadigini
    # gostermeye yarar(True/False)
    return {
        "Id":id,
        "Comment_Titie":comment_title,
        "Blog":blog,
        "Content":content,
        "Version":version,
        "Comment_Id":comment_id,
        # "Version_2": version_2,
        # "Content_2":content_2,
    }






