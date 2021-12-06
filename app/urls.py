from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path
urlpatterns=[
  path('search/', views.search_results, name='search_results'),
  path('', views.home, name='home'),
  path('user/', views.profile, name='profile'),
  path('user/addimage', views.add_image, name='addimage'),
  path('user/updateprofile', views.update_profile, name='updateprofile'),
  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)