from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Posts, Comment
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'name', 'comment', 'created_at']



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise serializers.ValidationError("Invalid username or password")
        else:
            raise serializers.ValidationError("Must include both username and password")

        return data  



# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField(required=True)
#     password = serializers.CharField(write_only=True, required=True)

#     def validate(self, data):
#         username = data.get('username')
#         password = data.get('password')

#         if username and password:
#             user = authenticate(username=username, password=password)
#             if not user:
#                 raise serializers.ValidationError("Invalid username or password")
#         else:
#             raise serializers.ValidationError("Must include both username and password")

#         refresh = RefreshToken.for_user(user)
#         return {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#             'username': user.username,
#             'email': user.email,
#             'lastname': user.last_name,
#             'firstname': user.first_name
#         }

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class PostsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Posts
        fields = ['post_id', 'author', 'name', 'owner', 'title', 'post', 'email', 'created_at', 'updated_at', 'comment_count', 'views', 'share_count', 'comments']
        read_only_fields = ['author', 'comment_count', 'views', 'share_count', 'created_at', 'updated_at']

    def create(self, validated_data):
        request = self.context.get('request')

        # Check if user is authenticated
        if not request or not request.user.is_authenticated:
            raise serializers.ValidationError('User must be authenticated to create a post.')

        validated_data['author'] = request.user
        
        return Posts.objects.create(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = '__all__'