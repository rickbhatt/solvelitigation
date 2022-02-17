from django.urls import path

from . import views

from django.urls import path

from . import views


urlpatterns=[
    path('criminal', views.criminal_home, name= 'criminal'),
    path('criminalSearch', views.criminal_search),

]