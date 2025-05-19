""" 认证模块 """
import jwt
from django.conf import settings
from jwt import exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class UrlJwtAuthentication(BaseAuthentication):
    """ 认证 请求路径中获取token 都要改成return None """

    def authenticate(self, request):
        token = request.query_params.get('token')
        salt = settings.SECRET_KEY
        try:
            payload = jwt.decode(token, salt, ["HS256"])
        except exceptions.ExpiredSignatureError:
            return None
        except jwt.DecodeError:
            return None
        except jwt.InvalidTokenError:
            return None

        # 认证通过
        return payload, token

    def authenticate_header(self, request):
        return 'Bearer realm="API"'


class HeaderJwtAuthentication(BaseAuthentication):
    """ 认证 请求头中获取token 都要改成return None """

    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        # print('tokentokentoken', token)
        salt = settings.SECRET_KEY
        try:
            payload = jwt.decode(token, salt, ["HS256"])
        except exceptions.ExpiredSignatureError:
            return None
        except jwt.DecodeError:
            return None
        except jwt.InvalidTokenError:
            return None

        # 认证通过
        return payload, token

    def authenticate_header(self, request):
        return 'Bearer realm="API"'


class NotJwtAuthentication(BaseAuthentication):
    """ 请求头，url中都没有获取到token抛出异常 """

    def authenticate(self, request):
        raise AuthenticationFailed({'code': 1002, 'error': "认证失败"})

    def authenticate_header(self, request):
        return 'Bearer realm="API"'
