from django.shortcuts import render

# Create your views here.

import os

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.core.servers.basehttp import FileWrapper

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions

from vphhf_rest.sms.models import File
from vphhf_rest.sms.serializers import FileSerializer

    
    
# ListCreateAPIView to get easily a get and post method    
class FileList(generics.ListCreateAPIView): 
    """
    List all files on server and create new
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer
    #permission_classes = (permissions.IsAuthenticated,)    


class FileListDetail(APIView):
    """
     Get or delete the single resource by GlobalFileID 
    """
    # get the resource
    def get(self, request, pk, format=None):
        try:
            fileid = File.objects.get(id=pk)
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 

        serializerfileid = FileSerializer(fileid, context={'request': request})
        return Response(serializerfileid.data)
        
    # Delete the resource
    def delete(self, request, pk, format=None):
        try:
            fdfile = File.objects.get(id=pk).filepath # No select_related() in this example.  // use a try - block exception
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        File.objects.get(id=pk).delete()  # erase it from the database
        
        try: 
            os.remove(fdfile.path)
        except OSError:
	    pass
        
        return Response(status=status.HTTP_200_OK)

     
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      #IsOwnerOrReadOnly,)
                      

class FileListContentDetail(APIView):

    # Get request to download the file
    def get(self, request, pk, format=None):
        try:  
            fdfile = File.objects.get(id=pk).filepath # No select_related() in this example.  // use a try - block exception
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 

        #download a file
        filename = str(fdfile) # Select your file here.
        filename1 = os.path.basename(filename)
        wrapper = FileWrapper(fdfile)
        response = HttpResponse(wrapper, content_type='application/force-download')   # I need to know the content_type of the resource, probably from file?
        #response = HttpResponse(wrapper, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename1
        response['Content-Length'] = os.path.getsize(fdfile.path)
        return response


