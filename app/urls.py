from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path
urlpatterns=[
  path('search/', views.search_results, name='search_results'),
  path('', views.home, name='home'),
  path('accounts/profile/', views.profile, name='profile'),
  path('addimage/', views.add_image, name='addimage'),
  path('updateimage/', views.update_profile, name='updateimage'),
  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)