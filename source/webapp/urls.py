from django.urls import path, include
from webapp.views import ProductsView,ProductView
app_name = 'webapp'


urlpatterns = [
    path('', ProductsView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),

]
