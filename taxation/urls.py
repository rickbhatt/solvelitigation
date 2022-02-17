from django.urls import path

from . import views

from django.urls import path

from . import views


urlpatterns=[
    path('taxation', views.tax_home, name= 'taxation'),
    path('taxSearch', views.tax_search),

]