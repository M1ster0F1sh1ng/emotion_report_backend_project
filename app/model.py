from pydantic import BaseModel,Field
from typing import Annotated

class user_model(BaseModel):
    name : Annotated[str,Field(max_length=107)]
    psw : Annotated[str,Field(min_length=6)]


class classs(BaseModel):
    code : str
    msg : str

class usr(BaseModel):
    user_name : str
    psw : str

class BOOK(BaseModel):
    book_name :str = Field(min_length=2,max_length=255,description= " " )
    writer : Annotated[str, Field(min_length=2,max_length=255,description= " " )]
    price :int