# models.py
from django.db import models
from django.db.models import F
from django.contrib.auth.models import User  

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from models import UserProfile


class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    post = models.TextField()
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    comment_count = models.IntegerField(default=0, editable=False)
    views = models.IntegerField(default=0, editable=False)
    share_count = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.title





class Comment(models.Model):
    post = models.ForeignKey(Posts, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.post.title}'

@receiver(post_save, sender=Comment)
def update_comment_count_on_save(sender, instance, **kwargs):
    post = instance.post
    post.comment_count = post.comments.count()
    post.save()

@receiver(post_delete, sender=Comment)
def update_comment_count_on_delete(sender, instance, **kwargs):
    post = instance.post
    post.comment_count = post.comments.count()
    post.save()

    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE)
    relatedPosts = models.ManyToManyField(posts) 
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.CharField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_data = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'users{User.username}'
    
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_pser_rofile(sender, instance, **kvargs):
    instance.userprofile.save()