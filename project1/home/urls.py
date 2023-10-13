

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('index1/', views.index1, name='index1'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contact/',views.contact, name='contact'),
    
]
