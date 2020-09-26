from django.urls import path, include
from webapp.views import ProductsView, ProductView, ProductCreateView, ProductUpdateView
app_name = 'webapp'


urlpatterns = [
    path('', ProductsView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
]
