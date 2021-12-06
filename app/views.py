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
    form=CommentForm(request.POST)
    if form.is_valid():
        image=self.get_object()
    
   
    return render(request,'index.html',{'images':images})
def single_image(request,image_id):
    image=get_object_or_404(Image,id=image_id)
    comments=Comments.objects.filter(image=image).all()
    current_user=request.user
    if request.method =='POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            
            comment.image = image
            comment.save()
        return redirect('home')
    else:
        
        form = CommentForm()
    return render(request, 'image.html', {'image': image, 'form':form, 'comments':comments})
    


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
    return render(request, 'profile/profile.html', {"images": images, "profile": profile})
@login_required(login_url='/accounts/login/')
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
def update_profile(request):
  	#Get the profile
    current_user=request.user
    profile = Profile.objects.filter(id=current_user.id).first()
    if request.method == 'POST':
        profileform = UpdateProfileForm(request.POST,request.FILES,instance=profile)
        if  profileform.is_valid:
            profileform.save(commit=False)
            profileform.user=request.user
            profileform.save()
            return redirect('profile')
    else:
        form=UpdateProfileForm()
    return render(request,'profile/update_profile.html',{'form':form})
