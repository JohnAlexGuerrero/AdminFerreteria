# Generated by Django 4.2.3 on 2023-08-17 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employed', '0002_alter_user_num_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='document',
            field=models.CharField(choices=[('CC', 'Cedula de Ciudadania'), ('TI', 'Targeta de Identidad')], default=('CC', 'Cedula de Ciudadania'), max_length=20, verbose_name='documento'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_one',
            field=models.IntegerField(null=True, verbose_name='telefono 1'),
        ),
    ]