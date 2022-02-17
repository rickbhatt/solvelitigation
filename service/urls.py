from django.urls import path

from . import views

from django.urls import path

from . import views


urlpatterns=[
    path('service', views.service_home, name= 'service'),
    path('serviceSearch', views.service_search),

]