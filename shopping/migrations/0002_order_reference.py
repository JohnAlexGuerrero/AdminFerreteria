# Generated by Django 4.2.3 on 2023-08-02 16:56

from django.db import migrations, models
import shopping.models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='reference',
            field=models.CharField(default=shopping.models.get_reference_product, max_length=50, verbose_name='referencia'),
        ),
    ]
