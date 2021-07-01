from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.log,name="main"),
    # path('l1/',views.log,name="main"),
    path('blog/',include('blog.urls')),
    path('chat/',include('chat.urls')),
    path('login/',include('login.urls')),
    path('logout/',views.index,name="logout"),
    path('signup/',include('signup.urls')),
    path('videochat/',include('videochat.urls')),
]
