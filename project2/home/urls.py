from django.urls import path
from home import views

urlpatterns = [
         path('',views.home, name='home'),
         path('home',views.home, name='home'),
         path('aboutus/', views.aboutus, name='aboutus'),
         path('contact/',views.contact, name='contact'),
         path('search',views.search, name='search'),
         
         path('category/<int:pkid>',views.show_category,name='show_category'),
]