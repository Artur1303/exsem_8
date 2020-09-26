from django.urls import path, include
from webapp.views import ProductsView
app_name = 'webapp'


urlpatterns = [
    path('', ProductsView.as_view(), name='index'),

]
