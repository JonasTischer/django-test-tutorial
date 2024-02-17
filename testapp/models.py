# testapp/models.py
from django.db import models
from django.contrib.auth.models import User  # Assuming standard User model

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)