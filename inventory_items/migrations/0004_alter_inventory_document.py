# Generated by Django 4.0.1 on 2022-01-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_items', '0003_alter_inventory_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='document',
            field=models.ImageField(upload_to=''),
        ),
    ]
