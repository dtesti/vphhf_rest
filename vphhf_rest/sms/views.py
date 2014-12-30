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

from vphhf_rest.sms.models import Document
from vphhf_rest.sms.serializers import DocumentSerializer

    
    
# ListCreateAPIView to get easily a get and post method    
class DocumentList(generics.ListCreateAPIView): 
    """
    List all documents on server and create new
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    #permission_classes = (permissions.IsAuthenticated,)    


class DocumentListDetail(APIView):
    """
     Get or delete the single resource by GlobalFileID 
    """
    # get the resource
    def get(self, request, pk, format=None):
        try:
            fileid = Document.objects.get(id=pk)
        except Document.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 

        serializerfileid = DocumentSerializer(fileid)
        return Response(serializerfileid.data)
        
    # Delete the resource
    def delete(self, request, pk, format=None):
        try:
            fdfile = Document.objects.get(id=pk).url # No select_related() in this example.  // use a try - block exception
        except Document.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        Document.objects.get(id=pk).delete()  # erase it from the database
        
        try: 
            os.remove(fdfile.path)
        except OSError:
	    pass
        
        return Response(status=status.HTTP_200_OK)

     
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      #IsOwnerOrReadOnly,)
                      

class DocumentListContentDetail(APIView):

    # Get request to download the file
    def get(self, request, pk, format=None):
        try:  
            fdfile = Document.objects.get(id=pk).url # No select_related() in this example.  // use a try - block exception
        except Document.DoesNotExist:
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


