from django.db import models

class Post(models.Model):
    owner = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment_count = models.IntegerField(default=0, editable=False)
    views = models.IntegerField(default=0, editable=False)
    share_count = models.IntegerField(default=0, editable=False)

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
