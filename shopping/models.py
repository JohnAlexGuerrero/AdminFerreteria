from django.db import models

from inventory.models import Product

from django.urls import reverse


select_way_to_pay = (
    ('30','credito 30 dias'),
    ('45','credito 45 dias'),
    ('15','credito 15 dias'),
    ('Co','contado'),
)
class Providers(models.Model):
    name = models.CharField(("empresa"), max_length=50, unique=True)
    address = models.CharField(("direccion"), max_length=100, null=True)
    contact = models.CharField(("nombre de contacto"), max_length=50, null=False)
    phonenumber = models.CharField(("telefono"), max_length=20, unique=True)

    class Meta:
        verbose_name = ("Provider")
        verbose_name_plural = ("Providers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Providers_detail", kwargs={"pk": self.pk})

class Invoice(models.Model):
    provider = models.ForeignKey(Providers, verbose_name=("providers"), on_delete=models.CASCADE)
    number = models.CharField(("numero factura"), max_length=10, unique=True)
    created_at = models.DateField(("fecha"), auto_now_add=False)
    expiration_at = models.DateField(("vencimiento"), auto_now_add=False)
    pay_at = models.CharField(("forma de pago"), max_length=50, choices=select_way_to_pay, default=select_way_to_pay[0])
    total = models.DecimalField(("total"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = ("Invoice")
        verbose_name_plural = ("Invoices")

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse("Invoice_detail", kwargs={"pk": self.pk})


class ProductInvoice(models.Model):
    product = models.ForeignKey(Product, verbose_name=("products"), on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, verbose_name=("invoices"), on_delete=models.CASCADE)
    quantity = models.IntegerField(("cantidad"))
    price = models.DecimalField(("precio"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = ("ProductInvoice")
        verbose_name_plural = ("ProductInvoices")

    def __str__(self):
        return self.product.name

    def get_absolute_url(self):
        return reverse("ProductInvoice_detail", kwargs={"pk": self.pk})
