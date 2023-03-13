from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<item_id>/buy', views.add_item, name = 'buy_item'),
    path('<item_id>/remove', views.add_item, name = 'remove_item'),
    path('add/', views.add_item, name = 'add_item'),
    path('user/', views.add_item, name = 'user'),
    path('<shop/', views.add_shop, name = 'add_shop'),
    path('<analytics/', views.analytics, name = 'analytics'),
]