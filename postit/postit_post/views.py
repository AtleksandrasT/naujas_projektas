from django.shortcuts import render
from rest_framework import generics, permissions
from . import models, serialazers


class PostList(generics.ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serialazers.PostSerializer
    premission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)