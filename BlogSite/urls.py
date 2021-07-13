from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('sendcode/',views.sendcode,name="sendcode"),
    path('verify_code/',views.verify_code,name="verify_code"),
    path('login/',views.__login__,name="login"),
    path('logout/',views.__logout__,name="logout"),
    path('admin/', admin.site.urls),
    path('',views.index,name="main"),
    path('blog/',include('blog.urls')),
    path('chat/',include('chat.urls')),
    path('contact/',include('contact.urls')),
    path('signup/',views.signin,name="signup"),
    path('videochat/',include('videochat.urls')),
]
