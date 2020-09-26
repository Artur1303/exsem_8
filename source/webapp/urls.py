from django.urls import path, include
from webapp.views import ProductsView, ProductView, ProductCreateView, ProductUpdateView, ProductDeleteView
from webapp.views.review_view import ReviewCreateView, ReviewUpdateView, ReviewDeleteView

app_name = 'webapp'


urlpatterns = [
    path('', ProductsView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('review/add-product/<int:pk>/', ReviewCreateView.as_view(), name='review_create'),
    path('product/<int:pk>/update-review/', ReviewUpdateView.as_view(), name='review_update'),
    path('product/<int:pk>/delete-review/', ReviewDeleteView.as_view(), name='review_delete'),
]
