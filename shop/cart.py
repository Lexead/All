from decimal import Decimal
from django.conf import settings
from django.http import HttpRequest
from . import models


class Cart:
    def __init__(self, request: HttpRequest) -> None:
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, product, quantity=1, update_quantity=False):
        product_pk = str(product.pk)
        if product_pk not in self.cart:
            self.cart[product_pk] = {
                'quantity': 0, 'price': str(product.price)}

        if update_quantity:
            self.cart[product_pk]['quantity'] = quantity
        else:
            self.cart[product_pk]['quantity'] += quantity

        self.save()

    def remove(self, product):
        product_pk = str(product.pk)
        if product_pk in self.cart:
            del self.cart[product_pk]
            self.save()

    def __iter__(self):
        product_pks = self.cart.keys()
        products = models.Product.objects.filter(pk__in=product_pks)
        for product in products:
            self.cart[str(product.pk)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
