from unicodedata import name
from django.urls import path

from . import views

urlpatterns=[
    path('sub-selection', views.sub_selection, name= 'sub-selection'),
    path ('successfulpay', views.successpay , name= "successful"),
    path('pay',views.pay, name='pay'),
    path('handlerequest', views.handlerequest, name='handlerequest')
]