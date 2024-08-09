# serializers.py
from rest_framework import serializers
from .models import BlogPost, PostForm

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']

class PostFormSerialiZer(serializers.ModelSerializer):
    class Meta:
        model = PostForm
        fields = ['id', 'name', 'email', 'message']
