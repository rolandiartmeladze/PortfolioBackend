# serializers.py
from rest_framework import serializers
from .models import BlogPost, PostForm, WriteNewPost, Comment

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']
        

class PostFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostForm
        fields = ['id', 'name', 'email', 'message']


# /serializer.py

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'name', 'comment', 'created_at']
        

class WriteNewPostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = WriteNewPost
        fields = ['post_id', 'name', 'owner', 'title', 'post', 'email', 'created_at', 'updated_at', 'comment_count', 'views', 'share_count', 'comments']

    def create(self, validated_data):
        # Create the WriteNewPost instance
        post = WriteNewPost.objects.create(**validated_data)
        
        # Initialize with an empty comment list (comments can be added later)
        post.comments.set([])  # Set empty comments initially
        
        return post

