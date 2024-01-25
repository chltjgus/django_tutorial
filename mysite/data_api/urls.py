from django.urls import path
from . import views

urlpatterns =[
    path('jeju/list', views.call_api_jeju, name='call_api_jeju'),
]