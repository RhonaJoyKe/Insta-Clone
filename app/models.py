from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'pictures/')
    # image = CloudinaryField('pictures')
    name = models.CharField(max_length =30)
    caption = models.TextField()
    profile = models.ForeignKey('Profile',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to = 'pictures/')
    bio=models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.bio
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.image
class Likes(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.image

