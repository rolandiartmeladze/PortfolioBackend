from django.contrib import admin
from .models import BlogPost, WriteNewPost, Comment

admin.site.register(BlogPost)
admin.site.register(WriteNewPost)
admin.site.register(Comment)
