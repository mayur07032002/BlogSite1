from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="signupmain"), 
    path("sign/",views.sign,name = "sign"),
    path("verify/",views.verify_email,name = "verification"),
]
