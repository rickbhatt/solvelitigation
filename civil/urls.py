from django.urls import path

from . import views

# from .views import civil_search

urlpatterns=[
    path('civil', views.civil_home, name= 'civil'),
    path('civilSearch', views.civil_search),

]