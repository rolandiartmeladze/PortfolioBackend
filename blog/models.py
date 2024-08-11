# models.py
from django.db import models
from django.db.models import F
from django.contrib.auth.models import User  # Import the User model

class BlogPost(models.Model):
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to Django's User model
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # comment_count = models.IntegerField(default=0, editable=False)
    # views = models.IntegerField(default=0, editable=False)
    # share_count = models.IntegerField(default=0, editable=False)




    def __str__(self):
        return f'Post {self.id} - {self.title}'
    
    def increment_views(self):
        self.views += 1
        self.save()

    def increment_comment_count(self):
        self.comment_count += 1
        self.save()

    def increment_share_count(self):
        self.share_count += 1
        self.save()



class PostForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self):
        return self.name





# class WriteNewPost(models.Model):
#     post_id = models.UniqueConstraint()

#     name = models.CharField(max_length=200)
#     owner = models.CharField(max_length=100)
#     title = models.CharField(max_length=200)
#     post = models.TextField()
#     email = models.EmailField()

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     coments_on_Post = models.aggregates()
    
#     comment_count = models.IntegerField(default=0, editable=False)
#     views = models.IntegerField(default=0, editable=False)
#     share_count = models.IntegerField(default=0, editable=False)


class WriteNewPost(models.Model):
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
    post = models.ForeignKey(WriteNewPost, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Increment the comment count correctly
        self.post.comment_count = F('comment_count') + 1
        self.post.save(update_fields=['comment_count'])

    def __str__(self):
        return f'Comment by {self.name} on {self.post.title}'

    post = models.ForeignKey(WriteNewPost, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwrgs):
        super().save(*args, **kwrgs)
        self.post.comment_count = F('comment_counter') +1
        self.post.save()
    def _str_ (self):
        return f'Comment by {self.name} on {self.post.title}'