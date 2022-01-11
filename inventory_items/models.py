from django.db import models
from datetime import date

# Create your models here.

# Data models as per inventory item details
class Inventory(models.Model):
    date_added = models.DateField(default=date.today())
    item_code = models.TextField(max_length=500, unique=True)
    item_name = models.TextField(max_length=500)
    quantity = models.IntegerField()
    price = models.IntegerField()
    sales = models.IntegerField()
    location = models.TextField(max_length=50)
    document = models.ImageField(upload_to="item_image")

    def __str__(self):
        return self.name

