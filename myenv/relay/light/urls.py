#urls.py
from django.urls import path
from .views import Home, Data

urlpatterns = [
    path('', Home),
    path('data', Data),
]
