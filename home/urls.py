from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact_view, name='contact'),    
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('admin-panel/delete_message/<contact_id>/', views.delete_message, name='delete_message'),
]