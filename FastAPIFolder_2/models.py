from .database import Base
from sqlalchemy import Column, Integer, String, DateTime


class PostModel(Base):
    __tablename__ = "PostModel"
    ID = Column(Integer, primary_key=True, index=True)
    Title = Column(String)
    Content = Column(String)
    Author = Column(String)
    Image_Url = Column(String)
    Timestamp = Column(DateTime)
    # ayni zamanda tabloyu temsil eden kod dizini
    # tablo olusturduktan sonra calistirdigimiz boilerplate (models.Base.metadata.create_all(engine))
    # icin 'Base' sinifina ihtiyacimiz var

