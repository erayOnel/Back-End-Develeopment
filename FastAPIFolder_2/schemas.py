from pydantic import BaseModel
from datetime import datetime


class PostSchema(BaseModel):
    Title: str
    Content: str
    Author: str
    Image_Url: str


class PostDisplay(BaseModel):
    ID: int
    Title: str
    Content: str
    Author: str
    Timestamp: datetime
    Image_Url: str

    class Config:
        orm_mode = True
