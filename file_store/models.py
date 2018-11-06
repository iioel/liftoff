import uuid, time
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
#from django.core.urlresolvers import resolve
from django.db import models

# Create your models here.

fs = FileSystemStorage(location='/var/local/liftoff')

class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    date = models.DateTimeField(auto_now_add=True)
    file_path = models.FileField(storage=fs, null=True)
    tags = models.ManyToManyField('Tag')

    class Meta:
        verbose_name = "file"
        ordering = ['date']

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=35)

    class Meta:
        verbose_name = "tag"
        ordering = ['name']

#class DownloadToken(models.Model):
#    token = models.CharField(max_length=255)
#    download_file = models.ForeignKey(File, on_delete=models.CASCADE)
#    download_url = models.URLField(max_length=300)
#    used = models.BooleanField(default=False)
#
#    def save(self, *args, **kwargs):
#        if not self.token:
#            self.token = uuid4()
#        self.download_url = download_file.url()
#
#        return super(DownloadToken, self).save(*args, **kwargs)
#
#
#def retrieve_token(request, token=''):
#    download_token = DownloadToken.objects.filter(token=token, used=False)
#    if download_token:
#        download_token = download_token[0] # Replace queryset with model instance
#        download_token.used = True
#        download_token.save()
#        response = resolve(download_token.download_url)
#        #response = HttpResponse(download_token.download, content_type='text/plain')
#        #response['Content-Disposition'] = 'attachment; filename=download.zip'
#        return response
#    else:
#        return HttpResponse(status_code=404)
