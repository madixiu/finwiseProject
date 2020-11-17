import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) 
    email = models.EmailField(blank=False, max_length=254, verbose_name="email address")
    phone_number = models.CharField(max_length =11,default = None,null = True,unique=True,error_messages={ 'unique':_("A user with that phonenumber already exists."),},)
    role = models.IntegerField(default = 1 , null = False)
    balance = models.FloatField(default = 0)
    expiration_date = models.DateTimeField(default = None, auto_now=False, auto_now_add=False, null = True)
    gender = models.CharField(max_length = 6, blank = True, null = True)
    birth = models.DateField(default = None, auto_now=False, auto_now_add=False, null = True)
    age = models.CharField(blank = True, null = True ,max_length=10, validators=[MinLengthValidator(10)])
    degree = models.CharField(max_length =20, blank = True, null = True)

    USERNAME_FIELD = "username"   # e.g: "username", "email"
    EMAIL_FIELD = "email"         # e.g: "email", "primary_email"   
    # PHONENUMBER_FIELD = "phone_number"
    # BIRTH_FIELD = "birth_date"