from django.db import models

# Create your models here.


class Document(models.Model):
    url = models.FileField( ('file'), upload_to='documents/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True, auto_now=True)
    
    class Meta:
        ordering = ('created',)

