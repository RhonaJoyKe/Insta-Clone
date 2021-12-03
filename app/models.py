from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'pictures/')
    # image = CloudinaryField('pictures')
    image_name = models.CharField(max_length =30)
    image_caption = models.TextField()
    profile = models.ForeignKey('Location',on_delete=models.CASCADE)
    likes=models.IntegerField(default=0)
    comments=models.IntegerField()
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to = 'pictures/')
    bio=models.TextField()