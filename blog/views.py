from rest_framework import viewsets
from django.shortcuts import render
from django.http import JsonResponse
from .models import Posts, Comment
from .serializers import PostsSerializer, CommentSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse






class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    # WriteNewPostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


