from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    author=models.CharField(max_length=100)
    timestamp=models.DateTimeField(auto_now=True)
    title=models.CharField(max_length=100)
    slug=models.CharField(max_length=100)
    content=models.TextField()
    

class Comments(models.Model):
    comment_id=models.AutoField(primary_key=True)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)



