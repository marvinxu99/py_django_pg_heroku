from django.urls import path, include, re_path

from . import views


app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
]
