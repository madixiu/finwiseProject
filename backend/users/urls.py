
from django.urls import path,re_path
from .views import verifyUser,passwordReset,test


urlpatterns = [
   # re_path(r'^get-token/$', get_csrf_token),
   path("verify", verifyUser),
   path("passwordReset",passwordReset),
   # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% test
   # path("test",test)

]
