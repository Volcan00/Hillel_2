from django.shortcuts import render
from django.http import HttpResponse
from .models import ShoppingList, MallList, Item, UserList

def index(request):
    user_list = UserList.objects.filter(user_id = 1).first()
    result = ShoppingList.objects.filter(list_id = user_list.list_id)
    new_result = [itm.__dict__ for itm in result]
    return HttpResponse("Hello it's shopping list!")

def add_item(request):
    return HttpResponse("Add Item")

def but_item(request):
    return HttpResponse("Buy Item")

def remove_item(request):
    return HttpResponse("Remove Item!")