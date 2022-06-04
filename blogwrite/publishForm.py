from django import forms

class PublishBlogForm(forms.Form):
    title = forms.CharField(label='title', max_length=100)
    author= forms.CharField(label='author', max_length=100)
    blog  = forms.CharField(label='blog', max_length=100)