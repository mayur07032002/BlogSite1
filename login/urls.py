from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="loginmain"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),     
    path("change/",views.change,name="change"),   
    path("sendcode/",views.send_code,name="sendcode"),   
    path("verify/",views.verify,name="verify"),   
    path('reset/',views.reset,name="reset"),
]
