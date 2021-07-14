from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="BlogHome"),
    path("<str:slug>",views.viewblog,name="viewblog"),
    path("writeblog/",views.write,name="writeBlog"),
]
