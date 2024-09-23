import logging

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly , IsAuthenticated
from rest_framework import views, viewsets, status, serializers, permissions
from rest_framework.response import Response 

from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.authtoken.models import Token

from rest_framework.response import Response
from django.contrib.auth import authenticate, login

from .models import Posts, Comment
from .serializers import PostsSerializer, CommentSerializer, UserSerializer, RegisterSerializer, LoginSerializer
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required


logger = logging.getLogger(__name__)






class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            if user:
                refresh = RefreshToken.for_user(user)
                logger.info(f"User {user.username} logged in successfully.")
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'username': user.username,
                    'email': user.email,
                    'lastname': user.last_name,
                    'firstname': user.first_name,
                }, status=status.HTTP_200_OK)
            else:
                logger.warning("Authentication failed: Invalid credentials.")
                return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)
        logger.error("Validation failed: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)









class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()  # Delete the token to log out
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"detail": "Token does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.validated_data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    


# class LogoutView(APIView):
    
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         logger.info(f"User {request.user} is logging out.")
#         try:
#             request.user.auth_token.delete()  
#             return Response({"message": "User logged out successfully"}, status=status.HTTP_200_OK)
#         except Exception as e:
#             logger.error(f"Error during logout: {str(e)}")
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # permission_classes = [IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# class CustomAuthToken(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         user = serializer.validated_data['user']

#         refresh = RefreshToken.for_user(user)

#         return Response({
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#             'username': user.username,
#             'email': user.email,
#             'lastname': user.last_name,
#             'firstname': user.first_name
#         }, status=status.HTTP_200_OK)





@login_required
def profile_view(request):
    user = request.user
    context = {
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        # Add other fields if needed
    }
    return render(request, 'profile.html', context)