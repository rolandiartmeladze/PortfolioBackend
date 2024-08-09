# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, PostFormViewSet, my_form_view

router = DefaultRouter()
router.register(r'posts', BlogPostViewSet)
router.register(r'forms', PostFormViewSet)  # Use a separate viewset for the form API

urlpatterns = [
    path('', include(router.urls)),  # Includes API root and all registered viewsets
    path('api/forms/', my_form_view, name='my-form-view'),  # Regular Django view for form
]
