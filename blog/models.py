from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField("Uploaded image", blank=True)   
    
