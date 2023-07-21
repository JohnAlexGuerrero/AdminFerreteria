from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(("categoria"), max_length=50, unique=True)
    slug = models.SlugField(("slug categoria"))

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})


class Product(models.Model):
    name = models.CharField(("descripcion"), max_length=100, unique=True)
    bar_code = models.CharField(("codigo"), max_length=50, unique=True)
    stock = models.IntegerField(("stock"), default=0)
    unit_measure = models.CharField(("unidad"), max_length=10)
    weight = models.FloatField(("peso"), default=0)
    cost = models.DecimalField(("costo"), max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField(("precio"), max_digits=10, decimal_places=2, default=0)
    category = models.ManyToManyField(Category)
    
    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})

