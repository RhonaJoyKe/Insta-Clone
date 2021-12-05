from django.shortcuts import get_object_or_404, render,redirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from .models import *
from .models import Image,Profile,Likes,Comments
from django.http  import HttpResponse,Http404
from django.contrib import messages


# Create your views here.
def home(request):
    images=Image.objects.all()
    
   
    return render(request,'index.html',{'images':images})

def search_results(request):

    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_images = Image.search_image(search_term)
        print(searched_images)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    images = Image.objects.filter(user=current_user)
    profile = get_object_or_404(Profile,id = current_user.id)
    return render(request, 'profile.html', {"images": images, "profile": profile})
def add_image(request):
    if request.method=='POST':
        current_user=request.user
        form=AddImageForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.user=current_user
            image.save()
            messages.success(request,('Image was posted successfully!'))
            return redirect('home')
    else:
            form=AddImageForm()
    return render(request,'add_image.html',{'form':form})