# # blog/urls.py
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import BlogPostViewSet, PostFormViewSet, my_form_view

# from blog.newPost.views import add_post
# from blog.addComment.views import add_comment

# router = DefaultRouter()
# router.register(r'posts', BlogPostViewSet)
# router.register(r'forms', PostFormViewSet)  


# urlpatterns = [
#     path('', include(router.urls)),  
#     path('api/forms/', my_form_view, name='my-form-view'),  
#     path('add-post/', add_post, name='add_post'),
#     path('post/<int:post_id>/comment/', add_comment, name='add_comment'),
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  PostsViewSet, CommentViewSet, UsersProfileViewSet
# from blog.newPost.views import add_post
# from blog.addComment.views import add_comment

router = DefaultRouter()
router.register(r'posts', PostsViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'users', UsersProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),  
    
]