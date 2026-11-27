from typing import Annotated
from fastapi import FastAPI, Path, Query, HTTPException, Depends
from fastapi.responses import FileResponse
from hashlib import sha1 as ha
from bcrypt import gensalt,hashpw,checkpw
import time
from pydantic import BaseModel,Field
import uvicorn

import model
app = FastAPI()


@app.middleware('http')
async def f(request,func_):
    print(f"a htpp request was active, at {time.time()}")
    response_ = await func_(request)
    return response_


@app.get("/")
async def root():
    return {"message": " hello_world "}

def name_get(id : int):
    return ha(id.__str__().encode()).hexdigest()

@app.get("/login/{id}")
async def funn(id : int = Path(gt=0)):
    str = name_get(id)
    if str=="" :
        raise HTTPException(status_code=503,detail="id非法输入")
    return {
        "user_name" : str,
        "id" : id
    }



async def psw_get(name : str):
    return b'$2b$12$sqfvIGhLdQTSkSA1.jKxg.MuneGU/PBMLVG9IKHg8yg/AFSd3TeNG'

@app.post("/login")
async def login_fun(user :model.user_model ):
    pw= await psw_get(user.name)
    return checkpw(user.psw.encode(),pw)


@app.get("/test/{id}")
async def funnn(id : int = Path(... , gt=1,lt=100, description="heima_test")):
    return {
        "msg" : f"{id} is better than 1,and less than 100"
    }

@app.get("/request")
async def funnnn(skip : int
                 ,nums : int
                 ):
    a=skip*nums
    b=(skip+1)*nums
    if (skip<0 or nums <1):
        raise HTTPException(status_code=403,detail="skip<0 or nums <1")
    return {
        "min_":a,
        "max" : b
    }


@app.get("/request/question")
async def funnnnn(price : Annotated[int ,Query(ge=50,le=100)] =None, type_ :  Annotated[ str ,Query(min_length=5,max_length=255)] ="Python kaifa" ):
    print(f"price: {price},type_: {type_}")
    return FileResponse("")#html,stream,json,file,




@app.post("/register/question",response_model=classs)
async def funnnnnn(user:model.usr):
    print(f"username:{user.user_name},psw:{user.psw}")
    return {
        "code" : "200",
        "msg": "success",
        "message " : "nice",
        "u_n" : f"{user.user_name}"
    }



@app.post("/add/question",response_model=model.classs)
async def funnnnnnn(Book : model.BOOK):
    return {
        "code" : "200",
        "msg": "success",
        "message " : "nice"
    }


@app.get("/test/depend")
async def func__(arg= Depends(model.BOOK)):
    return arg


if __name__== "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8500)