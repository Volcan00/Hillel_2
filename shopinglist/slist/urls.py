from django.urls import path

form  . import views

urlpatterns = [
    path('/', views.index, name = 'index'),
    path('add/', views.add_item, name = 'add_item'),
    path('<item_id>/buy', views.add_item, name = 'buy_item'),
    path('<item_id>/remove', views.add_item, name = 'remove_item'),
    path('user/', views.add_item, name = 'user'),
    path('<user_id>/add_shop', views.add_item, name = 'add_shop'),
    path('<user_id>/add_user', views.add_item, name = 'add_user'),
    path('<user_id>/remove', views.add_item, name = 'analytics'),

]