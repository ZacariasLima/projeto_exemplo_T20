from django.urls import path
from . import views

app_name = 'characters'

urlpatterns = [
    path('', views.home, name='home'),
    path('characters/<int:id>/', views.character, name='character'),
]