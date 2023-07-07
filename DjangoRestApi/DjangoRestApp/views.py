from django.shortcuts import render
from rest_framework import viewsets
 


# Create your views here.
class PostViewSets(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
