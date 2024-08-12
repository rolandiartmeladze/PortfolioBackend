# serializers.py
from rest_framework import serializers
from .models import Posts, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'name', 'comment', 'created_at']
        

class PostsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Posts
        fields = ['post_id', 'name', 'owner', 'title', 'post', 'email', 'created_at', 'updated_at', 'comment_count', 'views', 'share_count', 'comments']

    def create(self, validated_data):
        
        post = Posts.objects.create(**validated_data)
        
        
        post.comments.set([]) 
        
        return post

