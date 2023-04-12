from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_form_view, name='contact_form'),
    path('', views.index, name='index'),
    
    
    
]