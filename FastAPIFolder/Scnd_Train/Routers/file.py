from fastapi import APIRouter, File, UploadFile
import shutil
from fastapi.responses import FileResponse

router = APIRouter(
    tags=["File"],
    prefix="/file"
)


@router.post("/")
def get_file(file: bytes = File(...)):
    content = file.decode("utf-8")
    return {"Content": content}


@router.post("/upload")
def get_uploadfile(upload_file: UploadFile = File(...)):
    # path = f"C:/Users/erayo/PycharmProjects/pythonProject/FastAPIFolder/Scnd_Train/Files/{upload_file.filename}"
    path = f"Files{upload_file.filename}"
    # path olarak belirtilen parametre dosyanin bulundugu konumu ifade ediyor
    # bu yuzden 'filename'in tanimlanmasi gerekiyor
    with open(path, "w+b") as buffer:
        # ('w',writing) dosyayi olusturur varsa belirler ve ('b',binary) dosyayi binary modda acar
        shutil.copyfileobj(upload_file.file, buffer)
        # 'shutil' fonksiyonu dosyalari kopyalamak,arsivlemek vb... gorevler icin kullanilir

    return {
        "Filename": path,
        "Type": upload_file.content_type
    }


@router.get("/from_api/{name}", response_class=FileResponse)
def get_from_api(name: str):
    path = f"Files{name}"
    return path




