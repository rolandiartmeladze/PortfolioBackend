from django.contrib import admin
from .models import Posts, Comment, UserProfile

admin.site.register(Posts)
admin.site.register(Comment)
admin.site.register(UserProfile)
