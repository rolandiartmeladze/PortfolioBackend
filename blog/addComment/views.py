
# addComment/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from blog.newPost.models import Post

def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        name = request.POST['name']
        content = request.POST['content']
        Comment.objects.create(post=post, name=name, content=content)
        return redirect('post_detail', post_id=post.id)
    return render(request, 'addComment/add_comment.html', {'post': post})