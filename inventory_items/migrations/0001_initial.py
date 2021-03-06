# Generated by Django 4.0.1 on 2022-01-11 10:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(default=datetime.date(2022, 1, 11))),
                ('item_code', models.TextField(max_length=500, unique=True)),
                ('item_name', models.TextField(max_length=500)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('sales', models.IntegerField()),
                ('location', models.TextField(max_length=50)),
                ('document', models.FileField(upload_to='item_image/')),
            ],
        ),
    ]
