from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostsViewSet, CommentViewSet, UserViewset, RegisterView, CustomAuthToken, LogoutView, LoginView

# Create a router for ViewSets
router = DefaultRouter()
router.register(r'posts', PostsViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'users', UserViewset)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),  
    path('', include(router.urls)),
]
