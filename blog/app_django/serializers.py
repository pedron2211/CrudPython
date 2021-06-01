from rest_framework import serializers
from django.contrib.auth.models import User
from app_django.models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']     
class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    class Meta:
        model = Post
        fields = ['id', 'body', 'created', 'owner']
    