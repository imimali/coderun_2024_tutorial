from .views import index, inspect_request,register_user
from django.urls import path

urlpatterns = [
    path('index/', index, name='index'),
    path('inspect/', inspect_request, name='inspect_request'),
    path('register/', register_user, name='register_user'),
]
