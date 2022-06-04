from django.shortcuts import render
from .models import Blog
from rest_framework import generics
from .serializers import BlogDetailSerializers
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class BlogCreateView(generics.CreateAPIView):
    serializer_class = BlogDetailSerializers


class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializers
    permission_classes = (IsAuthenticated, )

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogDetailSerializers
    queryset = Blog.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )

def index(request):
    data = Blog.objects.all()
    context = {
        'data' : data
    }
    return render(request,
                  template_name='index.html',
                  context=context)

def gallery(request):
    return render(request,
                  template_name='gallery.html')
