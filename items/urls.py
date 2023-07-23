from django.urls import path
from .views import ItemCreateView, ItemDeleteView, ItemDetailView, ItemListView, ItemUpdateView
urlpatterns = [
    path('', ItemListView.as_view(), name='items'),
    path('<pk>',ItemDetailView.as_view(), name="item_details"),
    path('create/', ItemCreateView.as_view(), name= 'item_create'),
    path('update/<pk>',ItemUpdateView.as_view(), name= 'item_update'),
    path('delete/<pk>',ItemDeleteView.as_view(), name= 'item_delete'),

]

