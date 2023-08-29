from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q
# Create your views here.

def index(request):
    post = Post.objects.all().order_by('?')
    category = Category.objects.all()

    query =request.GET.get("q")
    if query:
        post = post.filter(
            Q(postTitle__icontains=query)|
            Q(postText__icontains=query)|
            Q(category__title__icontains=query)
        ).distinct
    
    context= {
        'post':post,
        'category':category,
        'profil':profil
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

def detail(request, postTitle):
    post= Post.objects.get(postTitle=postTitle)
    category = Category.objects.all()
    comment = Comment.objects.filter(commentPost=post)
    

    if request.method =='POST':
        comment =request.POST['comment']
        comn = Comment(commentText=comment,commentPost=post,user=request.user)
        comn.save()
        
        return redirect('/detay/' + post.postTitle + '/')

    context={
        'post':post,
        'comment':comment,
        'category':category
    }
    return render (request,'detail.html',context)



def register(request):
    
    if request.method =='POST':
        name = request.POST['firstname']
        surname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password==password2:
            if User.objects.filter(username=name).exists():
                #* exists fonksiyonu ile veritabanında sorgulama yapılmaktadır.
                context = {
                    'information':'Bu kullanıcı sistemimizde mevcuttur. Farklı bir kullanıcı adı deneyiniz'
                }
                
                return render(request,'user/register.html',context)
            
            if User.objects.filter(email=email).exists():
                
                context = {
                    'information': 'Bu e-mail kullanılıyor. Farklı bir mail adresiyle kayıt olmayı deneyiniz.'
                }
                return render(request,'user/register.html',context)
            
            else:
                user = User.objects.create_user(username=name, email=email, first_name=name, last_name=surname,password=password)
                user.save()
                return redirect('kayıtol')
        else:
            context = {
                'information':'Parolanız tekrar parolanızla uyuşmuyor, tekrar kayıt olmayı deneyiniz.'
            }
            
            return render (request,'user/register.html',context)
    
    return render (request,'user/register.html')



def loginn(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('anasayfa')
        else:
            context = {
                'information': 'Girmiş olduğunuz bilgiler hatalı kullanıcı adı ve parolanızı kontrol ediniz.'
            }
            return render(request, 'user/login.html', context)
    
    return render(request, 'user/login.html')

def logoutt(request):
    
    logout(request)
    
    return redirect ('anasayfa')

@login_required(login_url='/girisyap/')
def profil(request):
    categories = Category.objects.all()
    
    user_profile=None
    if request.user.is_authenticated:
        try:
            user_profile = Profil.objects.get(user=request.user)
            
        except Profil.DoesNotExist:
            user_profile = Profil(user=request.user)
            user_profile.save()
            
    if request.method =='POST' and 'profil-img' in request.POST:
            file = request.FILES.get('image')
            if user_profile:
                user_profile.profil_img=file
                user_profile.save()
    
    
    if request.method == "POST" and "user" in request.POST:
        user = request.user
        user.username = request.POST['username']
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email = request.POST['email']
        
        user.save()
        
    if request.method == "POST" and "post" in request.POST:
        postTitle = request.POST['title']
        postText = request.POST['postText']
        postImg = request.FILES['postImg']
        category_id = request.POST['category']
        
        category = Category.objects.get(id=category_id)
        
        post= Post(postTitle=postTitle,postText=postText,postImg=postImg,category=category,user=request.user)
        
        post.save()
        
        return redirect('anasayfa')
        
    context = {
        'categories':categories,
        'user_profile':user_profile,
        'profil':profil
    }
    
    return render(request,'profil.html',context)

def liked(request, id):
    
    post = Post.objects.get(id=id)
    
    if request.user in post.liked.all():
        post.liked.remove(request.user)
        liked=True
        
    else:
        post.liked.add(request.user)
        liked=False
        
        
    post.like_count = post.liked.count()
    
    post.save()
    
    return redirect('anasayfa')

def trend(request):
    
    trend_post = Post.objects.filter(like_count__gte=3).order_by('-like_count')
    
    
    context = {
        'trend_post':trend_post
    }
    return render(request,'trends.html',context)