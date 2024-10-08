from django.urls import path

from user.views import loginUser, logoutUser, registerUser, userProfile


app_name = "user"

urlpatterns = [
    path('', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerUser, name='register'),
    path('profile/', userProfile, name='profile'),
]
