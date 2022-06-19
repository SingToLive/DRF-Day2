from unicodedata import category
from django.db import models
from user.models import CustomUser
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    discription = models.TextField(max_length=500, null=True)
    
class Article(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    content = models.TextField(max_length=3000)    