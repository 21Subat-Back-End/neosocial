from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def index(request):
    post = Post.objects.all()
    category = Category.objects.all()
    
    context= {
        'post':post,
        'category':category
    }
    return render(request,'index.html',context)

def category(request, id):
    post = Post.objects.filter(category=id)
    category = Category.objects.all()
    
    
    context = {
        'category':category,
        'post':post
    }
    return render (request,'category.html',context)

def detail(request, id):
    post= Post.objects.get(id=id)
    comment = Comment.objects.all()
    

    if request.method =='POST':
        comment =comment.request["comment"]
        comn = Comment.save

        redirect(request,'detail.html')
    
    context={
        'post':post,
        'comment':comment
    }
    return render (request,'detail.html',context)