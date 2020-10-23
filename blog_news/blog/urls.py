from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog-home") ,
    path('campgrounds-index', views.campgroundsindex, name="campgroundsindex") ,
    path('campgroundopen', views.campgroundopen, name="campgroundopen") ,

    
]
