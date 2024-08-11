from rest_framework import viewsets
from django.shortcuts import render
from django.http import JsonResponse
from .models import BlogPost, PostForm, WriteNewPost, Comment
from .serializers import BlogPostSerializer, PostFormSerializer, WriteNewPostSerializer, CommentSerializer
from .forms import MyForm

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer




class PostFormViewSet(viewsets.ModelViewSet):
    queryset = PostForm.objects.all()
    serializer_class = PostFormSerializer

class WriteNewPostViewSet(viewsets.ModelViewSet):
    queryset = WriteNewPost.objects.all()
    serializer_class = WriteNewPostSerializer
    # WriteNewPostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Form submitted successfully!'}, status=201)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = MyForm()
    return render(request, 'form_template.html', {'form': form})


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'posts': reverse('blogpost-list', request=request, format=format),
        'forms': reverse('postform-list', request=request, format=format),
        'add_post': reverse('add_post', request=request, format=format),
        'add_comment': reverse('add_comment', args=[1], request=request, format=format),
    })

