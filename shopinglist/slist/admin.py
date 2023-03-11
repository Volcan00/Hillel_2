from django.contrib import admin
from .models import ShoppingList, UserList, MallList, Item

admin.site.register(ShoppingList)
admin.site.register(UserList)
admin.site.register(MallList)
admin.site.register(Item)