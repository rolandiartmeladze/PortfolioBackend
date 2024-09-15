from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  PostsViewSet, CommentViewSet, RegisterView

router = DefaultRouter()
router.register(r'posts', PostsViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('accounts/register/', RegisterView.as_view(), name='register'),  
]


