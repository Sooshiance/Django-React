from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from .views import (UserRegisterGenericAPIView,
                    CustomTokenObtainPairView,
                    ProfileGenericAPIView,)


app_name = 'user'

urlpatterns = [
    path("register/", UserRegisterGenericAPIView.as_view(), name='register'),
    path("access/", CustomTokenObtainPairView.as_view(), name='access'),
    path("refresh/", TokenRefreshView.as_view(), name='refresh'),
    path("profile/", ProfileGenericAPIView.as_view(), name='profile'),
]
