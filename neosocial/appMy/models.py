from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(("Kategori"), max_length=50)
    
    def __str__(self) -> str:
        return self.title

class Post(models.Model):
    postTitle = models.CharField(("post baslığı"), max_length=50)
    postText = models.TextField(("post icerik"),null=True,blank=True)
    postImg = models.ImageField(("post fotoğrafı"), upload_to=None, height_field=None, width_field=None, max_length=None,null=True,blank=True)
    category = models.ForeignKey(Category, verbose_name=("Kategori adı"), on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.postTitle
    
class Comment(models.Model):
    commentText = models.TextField(("Yorum"))
    commentPost = models.ForeignKey(Post, verbose_name=("Post"), on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.commentText
    
# class User (models.Model):
#     image = models.FileField((""), upload_to=None, max_length=100,null=True,blank=True)
#     userPost = models.ForeignKey(Post, verbose_name=(""), on_delete=models.CASCADE, null=True,blank=True)
#     userComment = models.ForeignKey(Comment, verbose_name=(""), on_delete=models.CASCADE, null=True,blank=True)
    
    