# Generated by Django 4.2.3 on 2023-08-03 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0006_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='comments',
            field=models.CharField(max_length=200, null=True, verbose_name='observaciones'),
        ),
    ]