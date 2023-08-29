from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(("Kategori"), max_length=50)
    
    def __str__(self) -> str:
        return self.title

class Post(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE,null=True,blank=True)
    postTitle = models.CharField(("post baslığı"), max_length=50)
    postText = models.TextField(("post icerik"),null=True,blank=True)
    postImg = models.ImageField(("post fotoğrafı"), upload_to=None, height_field=None, width_field=None, max_length=None,null=True,blank=True)
    category = models.ForeignKey(Category, verbose_name=("Kategori adı"), on_delete=models.CASCADE,null=True,blank=True)
    postTime = models.DateTimeField((""), auto_now=False, auto_now_add=True,null=True,blank=True)
    liked = models.ManyToManyField(User,verbose_name=('Beğenenler'),related_name=("liked_post"))
    like_count = models.PositiveIntegerField(("Beğen sayısı"),default=0)

    
    def __str__(self) -> str:
        return self.postTitle
    
class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE,null=True,blank=True)
    commentText = models.TextField(("Yorum"))
    commentPost = models.ForeignKey(Post, verbose_name=("Post"), on_delete=models.CASCADE)
    commentTime = models.DateTimeField((""), auto_now=False, auto_now_add=True,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.commentText
    
class Profil(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE,null=True,blank=True)
    profil_img = models.ImageField(("Profil fotoğrafı"), upload_to=None, height_field=None, width_field=None, max_length=None)

    