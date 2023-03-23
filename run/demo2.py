#!usr/bin/env python
# -*- coding:utf-8 _*-

import uvicorn
from fastapi import FastAPI
from fastapi.testclient import TestClient
 
app = FastAPI()
 
 
@app.get("/")
async def read_main():
    return {"msg": "Hello World"}
 
 
# 声明一个 TestClient，把 FastAPI() 实例对象传进去
client = TestClient(app)
 
 
# 测试用
def test_read_main():
    # 请求 127.0.0.1:8080/
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
 
 
from typing import Optional
 
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
 
# 模拟真实 token
fake_secret_token = "coneofsilence"
 
# 模拟真实数据库
fake_db = {
    "foo": {"id": "foo", "title": "Foo", "description": "There goes my hero"},
    "bar": {"id": "bar", "title": "Bar", "description": "The bartenders"},
}
 
app = FastAPI()

class Item(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
 
 
# 接口一：查询数据
@app.get("/items/{item_id}", response_model=Item)
async def read_main(item_id: str, x_token: str = Header(...)):
    # 1、校验 token 失败
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="x-token 错误")
 
    # 2、若数据库没有对应数据
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="找不到 item_id")
    # 3、找到数据则返回
    return fake_db[item_id]
 

# 接口二：创建数据
@app.post("/items/", response_model=Item)
async def create_item(item: Item, x_token: str = Header(...)):
    # 1、校验 token 失败
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="x-token 错误")
 
    # 2、若数据库已经存在相同 id 的数据
    if item.id in fake_db:
        raise HTTPException(status_code=400, detail="找不到 item_id")
 
    # 3、添加数据到数据库
    fake_db[item.id] = item
 
    # 4、返回添加的数据
    return item
  
if __name__ == '__main__':

    print(111)
    uvicorn.run(app="demo2:app", reload=True, host="127.0.0.1", port=8080)

