from django.db import models
from django.db.models import F
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User  
from django.dispatch import receiver


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


# class Posts(models.Model):
#     post_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=200)
#     owner = models.CharField(max_length=100)
#     title = models.CharField(max_length=200)
#     post = models.TextField()
#     email = models.EmailField()

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     comment_count = models.IntegerField(default=0, editable=False)
#     views = models.IntegerField(default=0, editable=False)
#     share_count = models.IntegerField(default=0, editable=False)

#     def __str__(self):
#         return self.title





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



# class UserProfile(models.Model):
#     birth_date = models.DateField(null=True, blank=True)
#     profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     bio = models.TextField(blank=True, null=True)
#     location = models.CharField(max_length=255, blank=True, null=True)


#     def __str__(self):
#         return self.user.username

# # Signal to create or save a user profile
# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#     else:
#         instance.userprofile.save()



# class UserProfileRelatedPosts(models.Model):
#     userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     post = models.ForeignKey(Posts, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.userprofile.user.username} related to {self.post.title}'
