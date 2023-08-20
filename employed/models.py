from django.db import models
from django.urls import reverse

from django.contrib.auth.models import AbstractUser

type_document = (
    ('CC','Cedula de Ciudadania'),    
    ('TI','Tarjeta de Identidad'),    
)

class User(AbstractUser):
    document = models.CharField(("documento"), max_length=50, choices=type_document, default=type_document[0])
    num_document = models.IntegerField(("numero de identificacion"), unique=True, null=True)
    address = models.CharField(("direccion"), max_length=50, null=True)
    phone_one = models.CharField(("telefono 1"), max_length=20, null=True)
    phone_two = models.CharField(("telefono 2"), max_length=20, null=True)
    created_at = models.DateField(("creacion"), auto_now_add=True)
    updated_at = models.DateField(("actualizacion"), auto_now_add=True)

    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("Person_detail", kwargs={"pk": self.pk})
