from unicodedata import category
from rest_framework import serializers
from .models import CustomUser as CustomUserModel
from blog.models import Article as ArticleModel
from blog.models import Comment as CommentModel
from blog.models import Category as CategoryModel

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ['article', 'contents']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['name', 'discription']

class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = ArticleModel
        fields = ['name', 'content', 'category']

class CustomUserSerializer(serializers.ModelSerializer):
    article_set = ArticleSerializer(many=True)
    comment_set = CommentSerializer(many=True)
    class Meta:
        model = CustomUserModel
        fields = ['username', 'join_date', 'article_set', 'comment_set']