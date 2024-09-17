from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User


def get_all_users():
    return User.objects.all()

class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    post_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=100)
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
    name = models.CharField(max_length=50)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.post.title}'


@receiver(post_save, sender=Comment)
@receiver(post_delete, sender=Comment)
def update_comment_count(sender, instance, **kwargs):
    post = instance.post
    post.comment_count = post.comments.count()
    post.save()
