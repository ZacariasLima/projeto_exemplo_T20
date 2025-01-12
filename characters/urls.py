from django.urls import path
from characters.views import home

urlpatterns = [
    path('', home),
]