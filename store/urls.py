from django.urls import path

from . import views

urlpatterns = [
  
    path('', views.store, name='store'),

    path('product/<slug:product_slug>/', views.product_info, name='product-info'),

    path('search/<slug:category_slug>/', views.list_category, name='list-category'),
    path('images/<str:image_name>/', views.serve_image_view, name='serve_image'),

]

