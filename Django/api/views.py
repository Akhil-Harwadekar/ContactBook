from django.shortcuts import render
from rest_framework import viewsets
from .models import Contacts
from .serializers import ContactSerializer

# Create your views here.
class ContactView(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer

