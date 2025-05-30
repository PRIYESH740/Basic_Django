from django.urls import path
from .views import *

urlpatterns = [
    path('api/some-data/', some_data_view, name='some-data'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
