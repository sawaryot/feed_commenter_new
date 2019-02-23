from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('girls_channel', views.girls_channel, name='girls_channel')
]