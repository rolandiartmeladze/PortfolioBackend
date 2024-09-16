from rest_framework import serializers
from .models import Posts, Comment
# import base64
# from django.core.files.base import ContentFile
# from django.contrib.auth.models import User
# from django.contrib.auth.password_validation import validate_password
  
from io import BytesIO
from PIL import Image




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


# class UserProfileSerializer(serializers.ModelSerializer):
#     user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     profile_picture = serializers.SerializerMethodField()

#     class Meta:
#         model = UserProfile
#         fields = ['user', 'bio', 'location', 'birth_date', 'profile_picture']

#     def get_profile_picture(self, obj):
#         if obj.profile_picture:
#             return obj.profile_picture.url
#         return None

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         if instance.profile_picture and not instance.profile_picture.url:
#             # Assuming the picture is stored as base64
#             representation['profile_picture'] = self.encode_image(instance.profile_picture)
#         return representation

#     def encode_image(self, image):
#         if not image:
#             return None
#         with open(image.path, "rb") as img_file:
#             encoded_image = base64.b64encode(img_file.read()).decode('utf-8')
#         return f"data:image/{image.name.split('.')[-1]};base64,{encoded_image}"

#     def to_internal_value(self, data):
#         if 'profile_picture' in data and isinstance(data['profile_picture'], str):
#             data['profile_picture'] = self.decode_image(data['profile_picture'])
#         return super().to_internal_value(data)

#     def decode_image(self, image_data):
#         format, imgstr = image_data.split(';base64,')
#         ext = format.split('/')[-1]
#         img_data = base64.b64decode(imgstr)
#         file_name = f'temp_image.{ext}'
#         file = ContentFile(img_data, file_name)
#         return file

# class UserRegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)
#     is_superuser = serializers.BooleanField(default=False, write_only=True)  # New field for superuser creation

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'password2', 'is_superuser']  # Include is_superuser

#     def validate(self, attrs):
#         # Ensure that password and password2 match
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError({"password": "Passwords do not match."})
#         return attrs

#     def create(self, validated_data):
#         # Remove password2 from validated_data as it's not needed
#         validated_data.pop('password2')

#         # Check if we want to create a superuser
#         is_superuser = validated_data.pop('is_superuser', False)

#         # Create a superuser or a regular user depending on the flag
#         if is_superuser:
#             user = User.objects.create_superuser(
#                 username=validated_data['username'],
#                 email=validated_data['email'],
#                 password=validated_data['password']
#             )
#         else:
#             user = User.objects.create_user(
#                 username=validated_data['username'],
#                 email=validated_data['email'],
#                 password=validated_data['password']
#             )
        
#         return user
