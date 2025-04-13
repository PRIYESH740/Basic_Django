from . import views
from django.urls import path,include

urlpatterns = [
    path("",views.home,name="Home"),
    path('about/',views.about,name='about'),
    path('services/',views.services,name="services"),
    path('contact/',views.contact,name="contact"),
]