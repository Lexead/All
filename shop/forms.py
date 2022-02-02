from django import forms

from . import models


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        label='', widget=forms.NumberInput(attrs={'placeholder': 'Количество', 'min': 1, 'class': 'form-control border-primary'}))
    update_quantity = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput)


class OrderCreateForm(forms.ModelForm):
    delivery_place = forms.CharField(
        max_length=50, label='', widget=forms.TextInput(attrs={'placeholder': 'Место доставки', 'class': 'form-control border-primary'}))

    class Meta:
        model = models.Order
        fields = ['delivery_place']
