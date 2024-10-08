from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PostsViewSet, 
    CommentViewSet, 
    UserViewset, 
    RegisterView, 
    LogoutView, 
    LoginView,
    profile_view
    )
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
# Create a router for ViewSets
router = DefaultRouter()
router.register(r'posts', PostsViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'users', UserViewset)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'), 
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('profile/', profile_view, name='profile'),
    path('', include(router.urls)),
]
