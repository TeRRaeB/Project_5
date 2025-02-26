from django.urls import path
from . import views 
from .views import add_review

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('rate_product/<product_id>/', views.rate_product, name='rate_product'),
    path('product/<product_id>/add_review/', add_review, name='add_review'),
] 