from django.contrib import admin
from file_store.models import File, Tag
from django.contrib.auth.models import User

# Register your models here.

class FileAdmin(admin.ModelAdmin):
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#    title = models.CharField(max_length=256)
#    author = models.ForeignKey('User', on_delete=models.PROTECT)
#    date = models.DateTimeField(auto_now_add=True)
#    url = models.URLField(max_length=300)
#    tags = models.ManyToManyField('Tag')

    exclude = ('author',)
    list_display=('title', 'date')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

class TagAdmin(admin.ModelAdmin):
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#    name = models.CharField(max_length=35)

    list_display = ('name',)

admin.site.register(File, FileAdmin)
admin.site.register(Tag, TagAdmin)
