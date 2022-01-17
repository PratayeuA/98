from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContactSerializer
from main.models import Contact
# Create your views here.

class ContactViewSet(viewsets.ModelViewSet):
	queryset = Contact.objects.all().order_by('email')
	serializer_class = ContactSerializer