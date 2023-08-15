from django.shortcuts import render
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

def detail(request):
    
    
    return render (request,'detail.html')