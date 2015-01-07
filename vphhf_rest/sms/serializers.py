from django.forms import widgets

from rest_framework import serializers

from vphhf_rest.sms.models import File

       
# In the same way that Django provides both Form classes and ModelForm classes, 
# REST framework includes both Serializer classes, and ModelSerializer classes.

 
class FileSerializer(serializers.ModelSerializer):
  
    url = serializers.FileField(label='Select a file')
    is_encrypted = serializers.BooleanField(required=True, label='Have to be encrypted')
    md5sum = serializers.ReadOnlyField()
    size = serializers.ReadOnlyField()
    
    
    class Meta:
        model = File  
        fields = ('id', 'url', 'is_encrypted', 'md5sum', 'size', 'created') # fields for plural