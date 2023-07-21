# Generated by Django 4.2.3 on 2023-07-18 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='categoria')),
                ('slug', models.SlugField(verbose_name='slug categoria')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='descripcion')),
                ('bar_code', models.CharField(max_length=50, unique=True, verbose_name='codigo')),
                ('stock', models.IntegerField(default=0, verbose_name='stock')),
                ('unit_measure', models.CharField(max_length=10, verbose_name='unidad')),
                ('weight', models.FloatField(default=0, verbose_name='peso')),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='costo')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='precio')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]