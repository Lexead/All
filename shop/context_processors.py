from .cart import Cart
from .models import Brand, Category


def cart(request):
    return {'cart': Cart(request)}


def categories(request):
    return {'categories': Category.objects.all()}


def brands(request):
    return {'brands': Brand.objects.all()}
