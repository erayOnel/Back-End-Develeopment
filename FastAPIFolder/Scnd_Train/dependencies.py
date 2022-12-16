from fastapi import APIRouter
from fastapi.param_functions import Depends
from fastapi import Request
from .custom_log import log

router = APIRouter(
    prefix="/dependencies",
    tags=["Dependencies"],
    dependencies=[Depends(log)],
)
# 'dependencies' parametresi router icerisinde tanimli herhangi apiyle birlikte calistirilabilir 'Depends' fonskiyonudur


def convert_params(request: Request):
    query = []
    for key, value in request.query_params.items():
        query.append(f"{key} ---> {value}")
    return query


def convert_headers(request: Request, query=Depends(convert_params)):
    out_headers = []
    for key, value in request.headers.items():
        out_headers.append(f"{key} ---> {value}")
    return {
        "Headers": out_headers,
        "Query": query,
    }


@router.get("")
def get_items(query_1: str, query_2: str, headers=Depends(convert_headers)):
    return headers


class Account:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


@router.post("/new")
def create_user(name: str, email: str, password: str, account: Account = Depends()):
    return {
        "Name": account.name,
        "Email": account.email,
    }

