from rest_framework.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView ,TokenRefreshView

urlpatterns= [
    path('register/',views.register_view,name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('token/',TokenObtainPairView.as_view(),name="token-auth"),
    path('token/refresh/',TokenRefreshView.as_view(),name='token-refresh'),
]