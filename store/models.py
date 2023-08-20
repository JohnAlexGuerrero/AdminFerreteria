from django.db import models
from django.urls import reverse

from employed.models import User

class Store(models.Model):
    name = models.CharField(("nombre"), max_length=50, unique=True)
    nit = models.CharField(("nit"), max_length=20,unique=True)
    address = models.CharField(("direccion"), max_length=50,unique=True, null=True)
    city = models.CharField(("ciudad"), max_length=50, null=True)
    email = models.EmailField(("email"), max_length=254)
    web = models.CharField(("pagina web"), max_length=250, unique=True, null=True)
    whatsapp = models.CharField(("whatsapp"), max_length=10, null=True)
    phone_1 = models.CharField(("telefono 1"), max_length=10, null=True)
    phone_2 = models.CharField(("telefono 2"), max_length=10, null=True)
    created_at = models.DateField(("creacion"), auto_now_add=True)
    updated_at = models.DateField(("actualizacion"), auto_now_add=True)

    class Meta:
        verbose_name = ("Store")
        verbose_name_plural = ("Stores")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Store_detail", kwargs={"pk": self.pk})


class UserStore(models.Model):
    user = models.OneToOneField(User, verbose_name=("user"), on_delete=models.CASCADE)
    store = models.OneToOneField(Store, verbose_name=("store"), on_delete=models.CASCADE)
    created_at = models.DateField(("creacion"), auto_now_add=True)
    updated_at = models.DateField(("actualizacion"), auto_now_add=True)

    class Meta:
        verbose_name = ("UserStore")
        verbose_name_plural = ("UserStores")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("UserStore_detail", kwargs={"pk": self.pk})
