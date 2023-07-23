from django.shortcuts import render
from django.views.generic import ListView, DetailView , CreateView , DeleteView , UpdateView
from .models import item
from django.urls import reverse_lazy


class ItemListView (ListView):
    template_name = 'items/items_list.html'
    model = item

class ItemDetailView (DetailView):
    template_name = 'items/items_Detail.html'
    model = item

class ItemCreateView (CreateView):
    template_name = 'items/items_create.html'
    model = item
    fields = ['name','price','purcheser']

class ItemUpdateView (UpdateView):
    template_name = 'items/items_update.html'
    model = item
    fields="__all__"
    success_url=reverse_lazy('items')

class ItemDeleteView(DeleteView):
    template_name = 'items/items_delete.html'
    model = item
    success_url=reverse_lazy('items')