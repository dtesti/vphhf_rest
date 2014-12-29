from django.forms import widgets

from rest_framework import serializers

from vphhf_rest.sms.models import Document

       
# In the same way that Django provides both Form classes and ModelForm classes, 
# REST framework includes both Serializer classes, and ModelSerializer classes.

 
class DocumentSerializer(serializers.ModelSerializer):
    url = serializers.FileField(
        label='Select a file'
    )
    
    class Meta:
        model = Document  
        field = ('url') # fields for plural