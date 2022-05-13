from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Item, Warehouse
from django.urls import reverse_lazy

class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'item_detail.html'

class ItemUpdateView(UpdateView):
    model = Item
    fields = ('title', 'body', 'location',)
    template_name = 'item_edit.html'

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'item_delete.html'
    success_url = reverse_lazy('item_list')

class ItemCreateView(CreateView):
    model = Item
    template_name = 'item_new.html'
    fields = ('title', 'body', 'location',)

class LocationListView(ListView):
    model = Warehouse
    template_name = 'location_list.html'

class LocationDetailView(DetailView):
    model = Warehouse
    template_name = 'location_detail.html'

class LocationUpdateView(UpdateView):
    model = Warehouse
    fields = ('country', 'town',)
    template_name = 'location_edit.html'

class LocationDeleteView(DeleteView):
    model = Warehouse
    template_name = 'location_delete.html'
    success_url = reverse_lazy('location_list')

class LocationCreateView(CreateView):
    model = Warehouse
    template_name = 'location_new.html'
    fields = ('country', 'town',)