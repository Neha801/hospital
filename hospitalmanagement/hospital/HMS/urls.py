from django.urls import path
from . import views

urlpatterns = [
    path('', views.Navbar, name='Navbar'),
    path('visitor/',views.visitor,name='visitor'),
    path('Infrastructure/',views.Infrastructure,name='Infrastructure'),
    path('about/',views.about,name='about'),
    path('carrer/',views.carrer,name='carrer'),
    path('contact/',views.contact,name='contact'),
    path('appointment/',views.appointment,name='appointment'),
    path('insurance/',views.insurance,name='insurance'),
    path('checkup/',views.checkup,name='checkup'),
    path('special/',views.special,name='special'),
]