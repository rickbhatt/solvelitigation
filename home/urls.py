from django.urls import path

from . import views

urlpatterns=[
    path('', views.home, name= 'home'),
    path('launching/', views.launching_soon, name='launching'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('subscription/', views.subscription, name='subscription'),
]