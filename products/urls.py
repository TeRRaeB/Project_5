from django.urls import path
from . import views 
from .views import add_review, get_subcategories

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('get_subcategories/<category_id>/', get_subcategories, name='get_subcategories'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('rate_product/<product_id>/', views.rate_product, name='rate_product'),
    path('product/<product_id>/add_review/', add_review, name='add_review'),
] 