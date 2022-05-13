from xml.etree.ElementInclude import include
from django.urls import path
from .views import (
     ItemListView, 
     ItemUpdateView, 
     ItemDetailView, 
     ItemDeleteView,
     ItemCreateView,
     LocationDetailView,
     LocationUpdateView,
     LocationListView,
     LocationDeleteView,
     LocationCreateView,
)

urlpatterns = [
    path('item/<int:pk>/edit/', ItemUpdateView.as_view(), name='item_edit'), # new
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'), # new
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'), # new
    path('new/item', ItemCreateView.as_view(), name = 'item_new'),
    path('item/list', ItemListView.as_view(), name ='item_list'),
    path('location/<int:pk>/edit/', LocationUpdateView.as_view(), name='location_edit'), # new
    path('location/<int:pk>/', LocationDetailView.as_view(), name='location_detail'),
    path('location/<int:pk>/delete/', LocationDeleteView.as_view(), name='location_delete'), # new
    path('new/location', LocationCreateView.as_view(), name='location_new'),
    path('location/list', LocationListView.as_view(), name ='location_list'),
]