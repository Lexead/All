from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to="category_images", default="...")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to="brand_images", default="...")

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self) -> str:
        return self.title


class ProductImage(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(
        upload_to="product_images/%Y/%m/%d", default="...")

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    model = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    images = models.ManyToManyField(
        ProductImage, null=True)
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(
        Brand, related_name='products', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self) -> str:
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="profile_images/%Y/%m%d", default="...")

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self) -> str:
        return str(self.user)


class Order(models.Model):
    user = models.ForeignKey(
        User, related_name='orders', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    delivery_place = models.CharField(max_length=50)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        return str(self.pk)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказов'

    def __str__(self) -> str:
        return str(self.pk)

    def get_cost(self):
        return self.price * self.quantity
