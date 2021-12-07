from django.test import TestCase
from .models import Image,Profile,Likes,Comments
from django.contrib.auth.models import User

# Create your tests here.
class ImageTestCase(TestCase):

    def setUp(self):
        """
        Create a image for testing
        """
        self.user=User(username='Jojo',email='hhhhh2@gmail.com',password1='1234')
        self.image=Image(image='food.jpg',name='food',caption='pretty awesome',user=self.user)
        self.comment=Comments(image='food.jpg',user=self.user,content='yeahh')
        self.like=Likes(image='food.jpg',user=self.user)
    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.image,Image))
        self.assertTrue(isinstance(self.comment,Comments))
        self.assertTrue(isinstance(self.like,Likes))