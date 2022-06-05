from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import ListView
from .publishForm import  PublishBlogForm
from .models import Blog
# Create your views here.

def BlogView(request):
    object_list={}
    object_list=Blog.objects.all()
    if request.method=='POST':
        search_value=request.POST.get('search',"")
        object_list=Blog.objects.all().filter(author=search_value)
    if object_list is None:
        object_list={}
    return render(request,"home.html",{"sorted":False,"object_list":object_list})

def sort(request):
    object_list={}
    object_list=Blog.objects.all().order_by("author")
    
    
    if request.method=='POST':
        search_value=request.POST.get('search',"")
        object_list=Blog.objects.all().filter(author=search_value)
    if object_list is None:
        object_list={}
    return render(request,"home.html",{"sorted":True,"object_list":object_list})
    
def openForm(request):
    return render(request,"open_form.html")

def publish(request):
    if request.method=="POST":
        form=PublishBlogForm(request.POST)
        if form.is_valid():
            obj=Blog()
            obj.title=form.cleaned_data['title']
            obj.author=form.cleaned_data['author']
            obj.body=form.cleaned_data['blog']
            obj.save()
            return HttpResponseRedirect('/')
