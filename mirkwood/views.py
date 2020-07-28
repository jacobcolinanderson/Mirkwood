from django.shortcuts import render
from mirkwood.models import Person, Item
from rest_framework import viewsets
from mirkwood.serializers import PersonSerializer, ItemSerializer

# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    http_method_names = ['get', 'post', 'put']

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
