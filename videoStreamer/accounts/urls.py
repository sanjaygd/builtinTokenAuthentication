# urls.py
from django.urls import path
from .views import (
    UserLoginView,
    UserLogoutView, 
    RegisterUserView
)

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-login'),
]
