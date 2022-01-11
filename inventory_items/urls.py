from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"), # end point to add item in inventory
    path("get-item/<int:id>", get_items, name="get_item"), # end point to get item from inventory
    path('edit-item', edit_item, name="edit_item"),  # end point to edit item from inventory
    path('delete-item/<int:id>', delete_item, name="delete_item") # end point to delete item from inventory
]
