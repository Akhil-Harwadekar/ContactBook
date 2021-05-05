from rest_framework import serializers
from .models import Contacts

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contacts
        fields = ('id','url', 'fname', 'lname', 'emailid', 'mobile')