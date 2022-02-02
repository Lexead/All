from xml.etree.ElementInclude import include
from django.conf.urls import url
from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    url(r"^catalog/$", RedirectView.as_view(url="/")),
    url(r"^home/", RedirectView.as_view(url="/")),
    path("catalog/<int:pk>/", views.ProductDetailView.as_view(),
         name="product_detail"),
    path("catalog/search/", views.SearchResultView.as_view(), name="search"),
    path("catalog/search/category/<str:category_title>/",
         views.filter_by_category, name="filter_by_category"),
    path("catalog/search/brand/<str:brand_title>/",
         views.filter_by_brand, name="filter_by_brand"),
    url(r"^signup/$", views.SignUpView.as_view(), name="signup"),
    url(r"^login/$", views.LoginView.as_view(), name="login"),
    url(r"^cart/$", views.cart, name="cart"),
    url(r"^cart/add/(?P<product_pk>\d+)/$",
        views.cart_add_product, name="cart_add"),
    url(r"^cart/remove/(?P<product_pk>\d+)/$",
        views.cart_remove_product, name="cart_remove"),
    url(r'^orders/$', views.get_orders, name="orders"),
    url(r'^order/create/$', views.order_add, name='order_create'),
    url(r'^order/remove/(?P<pk>\d+)/$', views.order_remove, name='order_remove'),
]
