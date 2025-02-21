from django.contrib import admin
from django.urls import path
from . import views
from .views import contact_view

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', contact_view, name='contact'),
]
