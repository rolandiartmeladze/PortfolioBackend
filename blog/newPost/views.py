from django.shortcuts import render, redirect
from .models import Post
from django.urls import reverse

def add_post(request):
    if request.method == 'POST':
        owner = request.POST.get('owner', 'Anonymous')  # Use 'Anonymous' if no owner is specified
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        if title and content:
            # Create and save the new Post object to the database
            Post.objects.create(owner=owner, title=title, content=content)
            # Redirect to the list of posts after successfully adding a new post
            return redirect(reverse('blogpost-list'))
        
    return render(request, 'newPost/add_post.html')  # Render the form template
