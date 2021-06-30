from django.contrib import admin
from django.urls import path, include
from .views import Profile, calculate, contact, home


urlpatterns = [
	path('', home, name='homepage'),
	path('contact/', contact, name='contact us page'),
	path('<str:ref_id>/', calculate, name='calculate'),
]

