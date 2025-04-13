from django.urls import path
from . import views

app_name = 'hrms'
urlpatterns = [
    path('', views.index, name='index'),   
]