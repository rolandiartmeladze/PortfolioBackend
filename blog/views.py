# views.py
from rest_framework import viewsets
from django.shortcuts import render
from django.http import JsonResponse
from .models import BlogPost, PostForm
from .serializers import BlogPostSerializer, PostFormSerialiZer
from .forms import MyForm

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class PostFormViewSet(viewsets.ModelViewSet):
    queryset = PostForm.objects.all()
    serializer_class = PostFormSerialiZer

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
