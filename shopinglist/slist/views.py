from django.shortcuts import render
from django.http import HttpResponse
from .models import ShoppingList, MallList, Item, UserList

def index(request):
    user_list = UserList.objects.filter(user_id = 1).first()
    if request.method == 'POST':
        item_name = request.POST.get('item')
        amount = request.POST.get('amount')
        shop_id  = request.POST.get('shop')
        shop_objct = MallList.objects.filter(pk = int(shop_id)).first()
        item_ojct = Item(name = item_name, shop_id = shop_objct)
        item_ojct.save()

        new_item = ShoppingList(list_id = user_list.list_id, item_id = item_ojct, quantity = amount)
        new_item.save()

    result = list(ShoppingList.objects.filter(list_id = user_list.list_id).all())

    return render(request, 'item_form.html', {'shoping_list_data': new_result, "shops": MallList.objects.all().filter(list_id = user_list.list_id) })
def add_item(request):
    return HttpResponse("Add Item")

def but_item(request):
    return HttpResponse("Buy Item")

def remove_item(request):
    return HttpResponse("Remove Item!")