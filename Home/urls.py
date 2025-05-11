from . import views
from django.urls import path,include

urlpatterns = [
    path("",views.home,name="Home"),
    path('about/',views.about,name='about'),
    path('food/',views.food,name="food"),
    path('orders/',views.orders,name="orders"),
    path('delivery/',views.delivery,name="delivery"),
    path('contact/',views.contact,name="contact"),
    path('submitform/',views.submitform,name="submitform"),
    path('calculater/',views.calculater,name="calculater"),
]