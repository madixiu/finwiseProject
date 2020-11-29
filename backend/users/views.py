from django.http.response import JsonResponse
from django.shortcuts import render, resolve_url
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.parsers import JSONParser 
from graphql_auth.models import UserStatus
from django.http import HttpResponse
from django.core import signing
# from users.auth.Verification import 
from .models import CustomUser
from .auth.Verification import SendVerificationNumber
from .utils.util import VerifyToken
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
        # phone = CustomUser.objects.get(email="mahdi.moradi72@gmail.com")
        # print(phone.phone_number)
        data = JSONParser().parse(request)
        # print(request)
        # return HttpResponse("ok")
        if data.get('request') == "activation":
            verificationNumber = SendVerificationNumber(data.get('email'))
            cache.set(data.get('email'),str(verificationNumber))
            # return HttpResponse(str(verificationNumber))
            return HttpResponse("OK")
        if data.get('request') == "verification":
            verificationNumber = cache.get(data.get('email'))
            # print(verificationNumber)
            # print(data.get('number'))
            if verificationNumber == data.get('number'):
                user = CustomUser.objects.get(email = data.get('email'))
                username = user.username
                token = VerifyToken(username)
                return JsonResponse(["GRANTED",token],safe=False)
            else:
                return JsonResponse(["DENIED"],safe=False)
        # if data.get('request') == "check":
        #     if data.get("number") == verificationNumber:
        #         return HttpResponse("True")
        #     else:
        #         return HttpResponse("False")