from django.forms import widgets

from rest_framework import serializers

from vphhf_rest.sms.models import File

       
# In the same way that Django provides both Form classes and ModelForm classes, 
# REST framework includes both Serializer classes, and ModelSerializer classes.

 
class FileSerializer(serializers.HyperlinkedModelSerializer):
  
    filepath = serializers.FileField(label='Select a file', use_url=False)
    is_encrypted = serializers.BooleanField(required=True, label='Have to be encrypted')
    md5sum = serializers.ReadOnlyField()
    size = serializers.ReadOnlyField()
    
    # Hyperlink for downloading the file
    url = serializers.HyperlinkedIdentityField(view_name='file-content')
    
    class Meta:
        model = File  
        fields = ('url', 'id', 'filepath', 'is_encrypted', 'md5sum', 'size', 'created') # fields for plural