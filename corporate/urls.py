from django.urls import path

from . import views

# from .views import corporate_search

urlpatterns=[
    path('corporate', views.corporate_home, name= 'corporate'),
    path('corporateSearch', views.corporate_search),

]