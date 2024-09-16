from rest_framework import viewsets, status
from django.shortcuts import render
from .models import Posts, Comment
from .serializers import PostsSerializer, CommentSerializer, UserRegistrationSerializer

from django.contrib.auth.models import User



class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    # WriteNewPostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


