from django.http.response import JsonResponse
from django.shortcuts import render

from .models import Inventory
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


# end point : ""
# Will Add new Item in Inventory including image
def index(request):
    if request.method=="POST":
        item_code = request.POST.get('code')
        item_name = request.POST.get('name')
        item_quantity = request.POST.get('quantity')
        item_price = request.POST.get('price')
        item_sales = request.POST.get('sales')
        location = request.POST.get('locationn')
        docs = request.FILES
        document = docs.get('myfile')

        # Check if item with same code exists in database
        try:
            check_item = Inventory.objects.get(item_code=item_code)
            messages.info(request, "Item already exists")
            return redirect('/')
        except:
            new_inventory = Inventory(item_code=item_code,item_name=item_name,quantity=item_quantity,price=item_price,sales=item_sales,location=location,document=document)
            new_inventory.save()
            messages.info(request, "Item added in Inventory successfully")
            return redirect('/')
    else:
        all_items = Inventory.objects.all()
        context = {'all_items':all_items}
        return render(request, "inventory.html", context)


# endpoint : "get-item/<int:id" where id = item id
def get_items(request, id):
    # Get specific item details from models
    item = Inventory.objects.get(id=id)

    # send item details as json response
    context = {
        "id":id,
        "item_code": item.item_code,
        "item_name": item.item_name,
        "item_quantity": item.quantity,
        "item_price": item.price,
        "item_sales": item.sales,
        "location":item.location

    }
    return JsonResponse(context)


# endpint : "edit-item" id already included in api to hide id from API 
# Function to edit item from inventory
def edit_item(request):
    if request.method=="POST":
        slug = request.POST.get('id')
        item = Inventory.objects.get(id=slug)
        item.item_code = request.POST.get('item_code')
        item.item_name = request.POST.get('item_name')
        item.quantity = request.POST.get('item_quantity')
        item.price = request.POST.get('item_price')
        item.sales = request.POST.get('item_sales')
        item.location = request.POST.get('location')
        item.save()
        messages.info(request, "Item edited successfully")
        return redirect("/")
    else:
        all_items = Inventory.objects.all()
        context = {'all_items': all_items}
        return render(request, 'inventory.html', context)


# endpoint : "delete-item/<int:id>" where id = item id
# Function to delete item from Inventory model
def delete_item(request, id):
    item = Inventory.objects.get(id=id)
    item.delete()
    return redirect("/")
