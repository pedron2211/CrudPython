from django.db import models

# Create your models here.
class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=250)
    owner = models.ForeignKey('auth.User',related_name='post',on_delete = models.CASCADE)
    
