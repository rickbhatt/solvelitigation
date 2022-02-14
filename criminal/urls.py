from django.urls import path

from . import views

from django.urls import path

from . import views

# from .views import civil_search

urlpatterns=[
    path('criminal', views.criminal_home, name= 'criminal'),
    # path('criminalSearch', views.criminal_search),

]