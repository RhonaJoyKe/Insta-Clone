from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'pictures/')
    # image = CloudinaryField('pictures')
    image_name = models.CharField(max_length =30)
    image_caption = models.TextField()
    profile = models.ForeignKey('Profile',on_delete=models.CASCADE)
    likes=models.IntegerField(default=0)
    comments=models.IntegerField()
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to = 'pictures/')
    bio=models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE)
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    comment = models.CharField(max_length=50)
    comment_date = models.DateTimeField(auto_now_add=True)
class Likes(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    # likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

