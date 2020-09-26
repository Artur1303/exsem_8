from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product


class ProductsView(ListView):
    template_name = 'product/index.html'
    model = Product
    context_object_name = 'products'


class ProductView(DetailView):
    template_name = 'product/product_view.html'
    context_object_name = 'product'
    model = Product


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    template_name = 'product/create_view.html'
    form_class = ProductForm
    permission_required = 'webapp.add_product'




    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})
