from django.db import models

# Create your models here.

#md5
import hashlib
from django.core.files.storage import FileSystemStorage


class MediaFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name):
        return name

    def _save(self, name, content):
        if self.exists(name):
            # if the file exists, do not call the superclasses _save method
            return name
        # if the file is new, DO call it
        return super(MediaFileSystemStorage, self)._save(name, content)
      

class File(models.Model):
  
    # upload_to = 'your upload dir'; 
    url = models.FileField( ('file'), upload_to='documents/%Y/%m/%d', storage = MediaFileSystemStorage())
    is_encrypted = models.BooleanField(default=None)
    md5sum = models.CharField(max_length=36)
    #size = models.IntegerField(default=10)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True, auto_now=True) # datetime.now default value??
    
    
    def size(self):
        return self.url.size
    
    def save(self, *args, **kwargs):
        if not self.pk:  # file is new
            md5 = hashlib.md5()
            for chunk in self.url.chunks():
                md5.update(chunk)
            self.md5sum = md5.hexdigest()
        super(File, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ('created',)


