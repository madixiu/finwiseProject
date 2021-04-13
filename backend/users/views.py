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
from .auth.Verification import SendVerificationNumber,SendPasswordResetNumber
from .utils.util import VerifyToken,PasswordResetToken
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
        print(data)
        if data.get('request') == "activation":
            verifcationNumber = SendPasswordResetNumber(data.get('email'))
            cache.set(data.get('email'),str(verifcationNumber))
            return HttpResponse("OK")
        if data.get('request') == "verification":
            print("we are in verification")
            verifcationNumber = cache.get(data.get('email'))
            print("here is the verification number:")
            print(verifcationNumber)
            print("email is:")
            print(data.get('email'))
            print("whole data:")
            print(data)
            if verifcationNumber == data.get('number'):
                token = PasswordResetToken(data.get('email'))
                return JsonResponse(["GRANTED",token],safe=False)
            else:
                return JsonResponse(["DENIED"],safe=False)
        else:
            
            return HttpResponse("error")