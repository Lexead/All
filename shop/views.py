from django.http import HttpResponse, HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, ListView, DetailView, FormView
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST, require_GET
from shop.forms import CartAddProductForm, OrderCreateForm
from . import models
from .cart import Cart


class HomeView(ListView):
    model = models.Product
    template_name = 'home.html'
    context_object_name = 'products'

    def get_queryset(self):
        return models.Product.objects.all()[:40]


class ProductDetailView(DetailView, FormView):
    model = models.Product
    template_name = "product_detail.html"
    form_class = CartAddProductForm


class LoginView(LoginView):
    template_name = "login.html"


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"


class SearchResultView(ListView):
    model = models.Product
    template_name = 'catalog.html'
    context_object_name = 'products'

    def get_queryset(self):
        search_text = self.request.GET.get('search_text', None)
        if search_text:
            products = models.Product.objects.filter(
                title__icontains=search_text
            )
        return products


@require_GET
def filter_by_category(request, category_title):
    products = models.Product.objects.filter(
        category__title__icontains=category_title)
    context = {'products': products}
    return render(request, "catalog.html", context)


@require_GET
def filter_by_brand(request, brand_title):
    products = models.Product.objects.filter(
        brand__title__icontains=brand_title)
    context = {'products': products}
    return render(request, "catalog.html", context)


@require_POST
def cart_add_product(request, product_pk):
    cart = Cart(request)
    product = get_object_or_404(models.Product, pk=product_pk)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cl_data = form.cleaned_data
        cart.add(product=product,
                 quantity=cl_data['quantity'],
                 update_quantity=cl_data['update_quantity'])
    return redirect("cart")


@require_POST
def cart_remove_product(request, product_pk):
    cart = Cart(request)
    product = get_object_or_404(models.Product, pk=product_pk)
    cart.remove(product)
    return redirect("cart")


@require_GET
def cart(request):
    cart = Cart(request)
    context = {"cart": cart}
    return render(request, "cart.html", context)


def order_add(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                models.OrderItem.objects.create(
                    order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            cart.clear()
            return render(request, 'created_order.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'create_order.html',
                  {'cart': cart, 'form': form})


@require_GET
def get_orders(request):
    orders = models.Order.objects.filter(user=request.user)
    context = {"orders": orders}
    return render(request, "orders.html", context)


def order_remove(request, pk):
    order = models.Order.objects.get(pk=pk)
    order.delete()
    return redirect('orders')
