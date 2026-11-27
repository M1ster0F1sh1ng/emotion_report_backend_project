from pydantic import BaseModel,Field
from typing import Annotated
from datetime import datetime
class user_model(BaseModel):
    name : Annotated[str,Field(max_length=31,min_length=1)]
    psw : Annotated[str,Field(min_length=6)]

class user_mysql(BaseModel):
    name : Annotated[str,Field(max_length=31)]
    psw : Annotated[str,Field()]=None
    id : Annotated[int ,Field(gt=0)]



class TAG_MODEL(BaseModel):
    type_ : Annotated[int ,Field(gt=0)]
    type_name :Annotated[str,Field(max_length=127)]

class E_EVENT_MODEL(BaseModel):
    user_id : Annotated[int ,Field(gt=0)]
    value :Annotated[float,Field(gt=-100,lt=100)]
    comment : Annotated[str , Field(max_length=4095)]=None
    type_ : Annotated[int ,Field()] =None

class E_EVENT_MYSQL_MODEL(BaseModel):
    user_id : Annotated[int ,Field(gt=0)]=None
    event_id: Annotated[int, Field(gt=0)]=None
    value :Annotated[float,Field(gt=-100,lt=100)]=None
    comment : Annotated[str , Field(max_length=4095)]=None
    type_ : Annotated[int ,Field()] =None
    create_time : Annotated[datetime,Field()]=None

class classs(BaseModel):
    code : str
    msg : str

class BOOK(BaseModel):
    book_name :str = Field(min_length=2,max_length=255,description= " " )
    writer : Annotated[str, Field(min_length=2,max_length=255,description= " " )]
    price :int