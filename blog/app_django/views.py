from rest_framework import generics
from django.contrib.auth.models import User
from app_django.serializers import UserSerializer
from app_django.serializers import PostSerializer
from app_django.models import Post


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner = user)
        
