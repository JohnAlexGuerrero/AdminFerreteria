# Generated by Django 4.2.3 on 2023-08-17 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='nombre')),
                ('nit', models.CharField(max_length=20, unique=True, verbose_name='nit')),
                ('address', models.CharField(max_length=50, null=True, unique=True, verbose_name='direccion')),
                ('city', models.CharField(max_length=50, null=True, verbose_name='ciudad')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('web', models.CharField(max_length=250, null=True, unique=True, verbose_name='pagina web')),
                ('whatsapp', models.CharField(max_length=10, null=True, verbose_name='whatsapp')),
                ('phone_1', models.CharField(max_length=10, null=True, verbose_name='telefono 1')),
                ('phone_2', models.CharField(max_length=10, null=True, verbose_name='telefono 2')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='creacion')),
                ('updated_at', models.DateField(auto_now_add=True, verbose_name='actualizacion')),
            ],
            options={
                'verbose_name': 'Store',
                'verbose_name_plural': 'Stores',
            },
        ),
        migrations.CreateModel(
            name='UserStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='creacion')),
                ('updated_at', models.DateField(auto_now_add=True, verbose_name='actualizacion')),
                ('store', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.store', verbose_name='store')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'UserStore',
                'verbose_name_plural': 'UserStores',
            },
        ),
    ]