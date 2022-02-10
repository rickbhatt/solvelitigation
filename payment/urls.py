from django.urls import path

from . import views

urlpatterns=[
    path('sub-selection', views.sub_selection, name= 'sub-selection'),
    path('test-login', views.personal, name= 'test-login'),




]