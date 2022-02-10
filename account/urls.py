from django.urls import path

from . import views 

from .views import resend_otp



urlpatterns=[
    path('register', views.registerpage, name= 'register'),
    path('login', views.loginpage, name='login'),
    path('t-and-c', views.t_and_c, name='t-and-c'),
    path('logout', views.logoutUser, name='logout'),

    path('forget-password',views.forget_password, name='forget-password'),
    
    path('change-password/<token>/',views.change_password, name='change-password'),

    path('resendOTP', resend_otp)

]