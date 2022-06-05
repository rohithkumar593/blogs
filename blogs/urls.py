
from argparse import Namespace
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth
from django.urls import path, include
from users import views as users_view
from django.contrib.auth import views as auth_view
from two_factor.urls import urlpatterns as tf_urls
from blogwrite.views import openForm,sort

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blogwrite.urls',namespace="blogwrite"),name="blogwriter"),
    path('users/', include('users.urls')),
    
     path('', include(tf_urls)),
    path('login/', users_view.Login, name ='login'),
    path('sort/',sort,name="sort"),
    path('logout/',auth_view.LogoutView.as_view(),name="logout"),
    path('register/', users_view.register, name ='register'),
    path('form_open/',openForm,name="openform")
  
]

