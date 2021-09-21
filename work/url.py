from django.urls import path,include
from . import views
urlpatterns = [
   path('',views.home,name="home"),
   path('about',views.about,name="aboutus"),
   path('courses',views.course,name="course"),
   path('gallery',views.gallery,name="gallery"),
   path('contact',views.contact,name="contact"),
]
