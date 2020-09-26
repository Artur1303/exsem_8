from django import forms


from webapp.models import Product, Review, RAITING_CHOICES


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = []


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        exclude = ['author', 'product']