# Generated by Django 4.2.3 on 2023-08-02 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit_measure',
            field=models.CharField(default='und', max_length=10, verbose_name='unidad'),
        ),
    ]