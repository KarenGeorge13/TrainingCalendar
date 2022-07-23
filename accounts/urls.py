from django.urls import path
from django.conf import settings
from .views import register, authen, user_logout

urlpatterns = [
    path('register/', register, name='register'),
    path('authen/', authen, name='authen'),
    path('logout/', user_logout, name='logout'),
]
