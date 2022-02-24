from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from testApp.models import AddressBook
from testApp.serializers import AddressSerializer


# Create your views here.

class AddressCBV(ModelViewSet):
    queryset = AddressBook.objects.all()
    serializer_class = AddressSerializer