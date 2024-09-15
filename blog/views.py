from rest_framework import viewsets, status
from django.shortcuts import render
from .models import Posts, Comment
from .serializers import PostsSerializer, CommentSerializer, UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


# from rest_framework.response import Response
# from rest_framework.views import APIView
from django.contrib.auth.models import User
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt



class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    # WriteNewPostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer




class RegisterView(APIView):
    permission_classes = [AllowAny]  # Allows any user to access this view

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Save the user (or superuser)
            return Response({
                "message": "User registered successfully.",
                "user": {
                    "username": user.username,
                    "email": user.email,
                    "is_superuser": user.is_superuser
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
