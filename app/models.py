from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.forms import ModelForm
from django.dispatch import receiver
from django.db.models.signals import post_save




# Create your models here.
class Image(models.Model):
    image = CloudinaryField('pictures')
    image_date = models.DateTimeField(auto_now_add=True ,null=True)
    name = models.CharField(max_length =30)
    caption = models.TextField()
    user = models.ForeignKey(User,related_name="posts", on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name
    # save image
    def save_image(self):
        self.save()

    # delete image
    def delete_image(self):
        self.delete()

    # update image caption
    def update_caption(self, new_caption):
        self.image_caption = new_caption
        self.save()
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to = 'pictures/')
    bio=models.TextField()
    first_name=models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=20,null=True)
    user_name=models.CharField(max_length=20,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.bio
    def save_profile(self):
        self.save()

    # update profile
    def update_profile(self, name):
        self.name = name
        self.save()

     # delete profile from database
    def delete_profile(self):
        self.delete()
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    content=models.CharField(max_length=20,null=True)
    
    def __str__(self):
        return self.image
    def save_comments(self):
        self.save()

    # update comments
    def update_comments(self, name):
        self.name = name
        self.save()

     # delete comments from database
    def delete_comments(self):
        self.delete()
class Likes(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.image
    def save_likes(self):
        self.save()

    # update like
    def update_likes(self, name):
        self.name = name
        self.save()

     # delete like from database
    def delete_likes(self):
        self.delete()

class AddImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image','caption','name']
class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_photo']
class CommentForm(ModelForm):
    class Meta:
        model=Comments
        fields=['content']



