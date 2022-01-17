from rest_framework import serializers
from main.models import Contact


class ContactSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Contact
		fields = ('name', 'email', 'message')