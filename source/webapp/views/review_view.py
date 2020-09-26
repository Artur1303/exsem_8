from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView

from webapp.forms import ReviewForm
from webapp.models import Review, Product


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'review/create_view.html'
    form_class = ReviewForm

    def get_queryset(self):
        product = get_object_or_404(Product, name=self.kwargs['pk'])
        return Review.objects.filter(product=product)

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.product = product
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.product.pk})
