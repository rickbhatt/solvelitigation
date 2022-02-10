from django.urls import path

from . import views

urlpatterns=[
    path('professional-home', views.professional_home, name= 'professional-home'),
    path('detail-doc/<str:id>', views.detail_doc, name= 'detail-doc'), 

]