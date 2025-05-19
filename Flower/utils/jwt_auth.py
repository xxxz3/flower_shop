# 生成token文件

import datetime

import jwt
from django.conf import settings


def create_token(payload, timeout=2):
    SALT = settings.SECRET_KEY
    # 构建header
    headers = {
        "alg": "HS256",  # 加密算法
        "typ": "jwt"
    }

    # 构建payload
    payload["exp"] = datetime.datetime.now() + datetime.timedelta(weeks=timeout)  # 超时时间
    # print(payload)
    token = jwt.encode(payload=payload, key=SALT, algorithm='HS256', headers=headers)
    return token
