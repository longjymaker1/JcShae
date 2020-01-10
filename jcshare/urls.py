from django.urls import path
from . import views


urlpatterns = [
    path('Hello_world', views.Hello_world, name='Hello_world'),
    path('', views.index, name='index'),
    path('base', views.base_test, name='base'),
]