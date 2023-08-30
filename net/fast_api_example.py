#!/bin/python3
"""
使用fastapi构建api接口
"""

from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import HTTPBearer
import uvicorn
import schedule
import string
import secrets
import time
import threading

app = FastAPI()
security = HTTPBearer()

token_store = {}


def random_token(length=16):
    """ 随机生成16位字符串 """
    characters = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(characters) for _ in range(length))
    return token


def expire_token(token):
    """ 删除过期token """
    try:
        token_store.remove(token)
        schedule.clear(token)
    except Exception as e:
        schedule.clear(token)


def verify_token(token: str = Depends(security)):
    """ 验证token """
    if token.credentials in token_store:
        return token.credentials
    else:
        raise HTTPException(status_code=401, detail="Invalid token")


@app.get("/get_msg")
def send_msg():
    """ get 请求 
        test: curl http://localhost:6003/get_msg
    """
    msg = {"code": 0, "msg": "hello world!"}
    return msg


@app.post("/get_form")
def send_form():
    """ post 请求 
        test: curl -X POST http://localhost:6003/get_form
    """
    form = {"code": 0, "msg": "get form successfully"}
    return form


@app.post("/generate_token")
def generate_token(request: Request):
    """ 获取请求token 
        test: curl -X POST http://localhost:6003/generate_token
    """
    resp_msg = {"result": None, "token": None}
    survival_time: int = 30000  # seconds
    client_ip = request.client.host
    try:
        token = random_token(16)
        token_store[token] = client_ip
        schedule.every(survival_time).seconds.do(expire_token,
                                                 token).tag(token)
        resp_msg["result"] = "generate token success"
        resp_msg["token"] = token
        # resp_msg["ip"] = client_ip
        print(token_store)
    except Exception as e:
        resp_msg["result"] = "Error: " + str(e)
    return resp_msg


@app.get("/protected_api")
def protected_api(token: str = Depends(verify_token)):
    """ 需要验证token的接口 
        test: curl -H "Authorization: Bearer v6DuUCigbSfcBmki" http://localhost:6003/protected_api
    """
    return {"msg": "Access granted"}


@app.post("/info")
def get_info(file: str, token: str = Depends(verify_token)):
    """ 带参数的请求 
        test: curl -H "Authorization: Bearer W51nNBxDtwNn5eMH" -X POST http://localhost:6003/info?file=test.file
    """
    resp = {file}
    return resp


@app.post("/test")
def get_info(file: str):
    resp = {file}
    return resp


def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    schedule_thread = threading.Thread(target=run_schedule)
    schedule_thread.start()
    uvicorn.run(app=app, host="0.0.0.0", port=6003, workers=1)