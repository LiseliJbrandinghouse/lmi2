from django.urls import path
from mysite import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
     path('make-appointment/', views.make_appointment, name='make_appointment'),
    path('confirm-appointment/<int:pk>/', views.confirm_appointment, name='confirm_appointment'),

]
  