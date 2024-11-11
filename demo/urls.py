from .views import index, inspect_request
from django.urls import path

urlpatterns = [
    path('index/', index, name='index'),
    path('inspect/', inspect_request, name='inspect_request'),
]
