from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    #path('/', views.item_list, name='item_list'),
    path('create/', views.create_item, name='create_item'),
    path('<int:item_id>/', views.get_item, name='get_item'),
    path('<int:item_id>/update/', views.update_item, name='update_item'),
    path('<int:item_id>/delete/', views.delete_item, name='delete_item'),
]