#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
"""
import os
import sys
ppath = os.path.dirname(os.path.realpath(__file__))
o_path= os.path.dirname(ppath)
sys.path.append(o_path)
from fastapi.testclient import TestClient
from run.demo2 import app
import pytest


client = TestClient(app)

def test_read_item():
    expect = {"id": "foo", "title": "Foo", "description": "There goes my hero"}
    headers = {"x-token": "coneofsilence"}
    resp = client.get("/items/foo", headers=headers)
    assert resp.status_code == 200
    assert resp.json() == expect
 
 
def test_read_item_error_header():
    expect = {"detail": "x-token 错误"}
    headers = {"x-token": "test"}
    resp = client.get("/items/foo", headers=headers)
    assert resp.status_code == 400
    assert resp.json() == expect
 
 
def test_read_item_error_id():
    expect = {"detail": "找不到 item_id"}
    headers = {"x-token": "coneofsilence"}
    resp = client.get("/items/foos", headers=headers)
    assert resp.status_code == 404
    assert resp.json() == expect
 
 
def test_create_item():
    body = {"id": "foos", "title": "Foo", "description": "There goes my hero"}
    headers = {"x-token": "coneofsilence"}
    resp = client.post("/items/", json=body, headers=headers)
    assert resp.status_code == 200
    assert resp.json() == body
 
 
def test_create_item_error_header():
    body = {"id": "foo", "title": "Foo", "description": "There goes my hero"}
    expect = {"detail": "x-token 错误"}
    headers = {"x-token": "test"}
    resp = client.post("/items/", json=body, headers=headers)
    assert resp.status_code == 400
    assert resp.json() == expect
 
 
def test_create_item_error_id():
    expect = {"detail": "找不到 item_id"}
    body = {"id": "foo", "title": "Foo", "description": "There goes my hero"}
    headers = {"x-token": "coneofsilence"}
    resp = client.post("/items/", json=body, headers=headers)
    assert resp.status_code == 400
    assert resp.json() == expect

if __name__=='__main__':

    pytest.main(['--report=musen.html',
             '--title=演示A报告',
             '--tester=测试员',
             '--desc=报告描述信息',
             '--template=2'])