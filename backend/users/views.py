from django.http.response import JsonResponse
from django.shortcuts import render, resolve_url
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
import json
import jwt
from rest_framework.parsers import JSONParser 
from graphql_auth.models import UserStatus
from django.http import HttpResponse
from django.core import signing
# from users.auth.Verification import 
from .models import CustomUser
from .auth.Verification import SendVerificationNumber,SendPasswordResetNumber
from .utils.util import VerifyToken,PasswordResetToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from django.core import signing

from graphql_jwt.utils import get_payload, get_user_by_payload,jwt_decode

# from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Create your views here.
# def get_token(self):
#     payload = {"username": "finwise", "action": "activation"}
#     token = signing.dumps(payload)
#     res = [token,SendVerificationNumber("fidel")]
#     # resp = json.loads(str(res))
#     return HttpResponse(res)
@csrf_exempt
def verifyUser(request):
    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        if data.get('request') == "activation":
            verificationNumber = SendVerificationNumber(data.get('email'))
            cache.set(data.get('email'),str(verificationNumber))
            return HttpResponse("OK")
        if data.get('request') == "verification":
            verificationNumber = cache.get(data.get('email'))

            if verificationNumber == data.get('number'):
                user = CustomUser.objects.get(email = data.get('email'))
                username = user.username
                token = VerifyToken(username)
                return JsonResponse(["GRANTED",token],safe=False)
            else:
                return JsonResponse(["DENIED"],safe=False)
@csrf_exempt
def passwordReset(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        if data.get('request') == "activation":
            verifcationNumber = SendPasswordResetNumber(data.get('email'))
            cache.set(data.get('email'),str(verifcationNumber))
            return HttpResponse("OK")
        if data.get('request') == "verification":
            # print("we are in verification")
            verifcationNumber = cache.get(data.get('email'))
            # print("here is the verification number:")
            # print(verifcationNumber)
            # print("email is:")
            # print(data.get('email'))
            # print("whole data:")
            # print(data)
            if verifcationNumber == data.get('number'):
                token = PasswordResetToken(data.get('email'))
                return JsonResponse(["GRANTED",token],safe=False)
            else:
                return JsonResponse(["DENIED"],safe=False)
        else:
            
            return HttpResponse("error")

# @permission_classes(IsAuthenticated, )
# def test(request):
#     tokenA = request.META.get('HTTP_AUTHORIZATION')[7:]
#     token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZpbndpc2UiLCJleHAiOjE2MjQxMTQ0ODAsIm9yaWdJYXQiOjE2MjQxMTMyMjB9.5oYk6hK_NPQ7mX5ETnNHbUsPg29uSeVhOyTuhEBLqRo"
#     # s = signing.dumps(payload,"#o&r+pyx=x(a^g!xxs6ntqls5dtad8y%q95sfcgekm-h7(6*+f")
#     print(tokenA[7:])
#     # # p="here"
#     # p = signing.loads(payload,"#o&r+pyx=x(a^g!xxs6ntqls5dtad8y%q95sfcgekm-h7(6*+f")
#     try:
#         payload = jwt_decode(tokenA)
#         username = payload["username"]
#         user = CustomUser.objects.get(username = username)
#         # print(user)
#         role = user.role
#         return JsonResponse(role,safe=False)
#     except:
#         return JsonResponse("notAuthorized",safe=False)


    