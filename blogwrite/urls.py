from django.contrib import admin
from django.urls import path,include
from .views import BlogView,openForm,publish
app_name='blogwrite'
urlpatterns = [
    path('form_open/publish/',publish),
    path('',BlogView)
    
]
