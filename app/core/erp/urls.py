from django.urls import path
from core.erp.views.category.views import *
from core.erp.views.marca.views import *
from core.erp.views.product.views import *


app_name = 'erp'

urlpatterns = [

    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),

    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    path('marca/list/', MarcaListView.as_view(), name='marca_list'),
    path('marca/add/', MarcaCreateView.as_view(), name='marca_create'),
    path('marca/update/<int:pk>/', MarcaUpdateView.as_view(), name='marca_update'),
    path('marca/delete/<int:pk>/', MarcaDeleteView.as_view(), name='marca_delete'),

    path('dashboard/', CategoryListView.as_view(), name='dashboard'),


]
