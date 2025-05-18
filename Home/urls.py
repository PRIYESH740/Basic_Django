from . import views
from django.urls import path,include

urlpatterns = [
    path("",views.home,name="Home"),
    path('about/',views.about,name='about'),
    path('food/',views.food,name="food"),
    path('order/<int:food_id>/', views.orders, name='orders'),
    path('orderSuccessful/<int:food_id>/', views.orderSuccessful, name='orderSuccessful'),
    path('delivery/<int:orderid>/',views.deliveryDetail,name="deliveryDetail"),
    path('delivery/',views.delivery,name="delivery"),
    path('contact/',views.contact,name="contact"),
    path('newsdetails/<slug>/',views.newsdetails),
    path('contactformsave/',views.contactformsave,name="contactformsave"),
    path('login/',views.login,name="login"),
]