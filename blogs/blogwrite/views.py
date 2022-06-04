from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import ListView
from .publishForm import  PublishBlogForm
from .models import Blog
# Create your views here.

class BlogView(ListView):
    model= Blog
    template_name= 'home.html'

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