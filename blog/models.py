from django.db import models
from user.models import CustomUser
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    discription = models.TextField(max_length=500, null=True)
    
    def __str__(self):
        return self.name
    
class Article(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField(max_length=3000)
    view_start_day = models.DateField(null=True)
    view_end_day = models.DateField(null=True)
    upload_date = models.DateField(null=True)
    def __str__(self):
        return f'{self.author} / {self.name} / {self.category} / {self.content}'
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    contents = models.TextField(max_length=3000, blank=True)
    
    def __str__(self):
        return f'{self.article} / {self.user} / {self.contents}'