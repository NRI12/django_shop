# Generated by Django 3.0.5 on 2024-02-29 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0011_auto_20240228_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(null=True),
        ),
    ]
