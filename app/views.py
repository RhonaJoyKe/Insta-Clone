from django.shortcuts import render,redirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from .models import *
from .models import Image,Profile,Likes,Comments
from django.http  import HttpResponse,Http404


# Create your views here.
def home(request):
    images=Image.objects.all()
    
   
    return render(request,'index.html',{'images':images})

# def search_results(request):

#     if 'name' in request.GET and request.GET["name"]:
#         search_term = request.GET.get("name")
#         searched_images = Image.search_image(search_term)
#         print(searched_images)
#         message = f"{search_term}"

#         return render(request, 'search.html',{"message":message,"images": searched_images})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'search.html',{"message":message})
# @login_required(login_url='/accounts/login/')
# def profile(request):
#     current_user=request.user
#     profile=Profile.objects.filter(user_id=current_user)
#     return render(request,'profile.html',{'profile':profile})
