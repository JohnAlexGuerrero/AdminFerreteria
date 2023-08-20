# Generated by Django 4.2.3 on 2023-08-17 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employed', '0003_alter_user_document_alter_user_phone_one'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='document',
            field=models.CharField(choices=[('CC', 'Cedula de Ciudadania'), ('TI', 'Targeta de Identidad')], default=('CC', 'Cedula de Ciudadania'), max_length=50, verbose_name='documento'),
        ),
    ]
