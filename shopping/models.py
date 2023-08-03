from django.db import models

from inventory.models import Product

from django.urls import reverse


select_way_to_pay = (
    ('30','credito 30 dias'),
    ('45','credito 45 dias'),
    ('15','credito 15 dias'),
    ('Co','contado'),
)


list_prices = (
    ('precio 1','30 %'),
    ('precio 2','20 %'),
    ('precio 3','15 %'),
    ('precio 4','10 %'),
    ('No','No aplica',),
)

def get_reference_product():
    return f'REF0031{Order.objects.all().count() + 2}'

class Providers(models.Model):
    name = models.CharField(("empresa"), max_length=50, unique=True)
    address = models.CharField(("direccion"), max_length=100, null=True)
    contact = models.CharField(("nombre de contacto"), max_length=50, null=True)
    phonenumber = models.CharField(("telefono"), max_length=20, unique=True, default='669999909')
    created_at = models.DateField(("creacion"), auto_now_add=True)
    updated_at = models.DateField(("creacion"), auto_now_add=True)

    class Meta:
        verbose_name = ("Provider")
        verbose_name_plural = ("Providers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Providers_detail", kwargs={"pk": self.pk})

class Invoice(models.Model):
    provider = models.ForeignKey(Providers, verbose_name=("providers"), on_delete=models.CASCADE)
    number = models.CharField(("numero factura"), max_length=20, unique=True)
    created_at = models.DateField(("fecha"), auto_now_add=False)
    expiration_at = models.DateField(("vencimiento"), auto_now_add=False)
    pay_at = models.CharField(("forma de pago"), max_length=50, choices=select_way_to_pay, default=select_way_to_pay[0])
    total = models.DecimalField(("total"), max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = ("Invoice")
        verbose_name_plural = ("Invoices")

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse("Invoice_detail", kwargs={"pk": self.pk})


class Order(models.Model):
    invoice = models.ForeignKey(Invoice, verbose_name=("invoices"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=("products"), on_delete=models.CASCADE)
    reference = models.CharField(("referencia"), max_length=50, default=get_reference_product)
    quantity = models.IntegerField(("cantidad"))
    price = models.DecimalField(("precio"), max_digits=10, decimal_places=2)
    total = models.DecimalField(("total"), max_digits=10, decimal_places=2, default=0)
    created_at = models.DateField(("created"), auto_now_add=False)

    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Orders")

    def __str__(self):
        return self.product.name

    def get_absolute_url(self):
        return reverse("ProductInvoice_detail", kwargs={"pk": self.pk})

class PriceProducts(models.Model):
    order = models.ForeignKey(Order, verbose_name=("product"), on_delete=models.CASCADE)
    price = models.DecimalField(("precio"), max_digits=10, decimal_places=2)
    utility = models.CharField(("utilidad"), max_length=50, choices=list_prices)

    class Meta:
        verbose_name = ("Price")
        verbose_name_plural = ("Prices")

    def __str__(self):
        return self.order.product.name

    def get_absolute_url(self):
        return reverse("Price_detail", kwargs={"pk": self.pk})