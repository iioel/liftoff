from django import forms
from file_store.models import *
from django.contrib.auth.models import User

def getTags():
    tags_name = []
    for tag in Tag.objects.all():
        tags_name.append((tag.id, tag.name))
    tags_name = tuple(tags_name)
    return(tags_name)

class FileForm(forms.ModelForm):
    title = forms.CharField(max_length=256)
    file_path = forms.FileField(required=False)
    tags = forms.MultipleChoiceField(choices=getTags())

    def __init__(self, *args, **kwargs):
        super(FileForm, self).__init__(*args, **kwargs)
        self.fields["tags"].choices = getTags()
        for name, field in self.fields.items():
#            if field.widget.__class__ == forms.widgets.TextInput:
            if 'class' in field.widget.attrs:
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs.update({'class':'form-control'})

    class Meta:
        model = File
        fields = ('title', 'file_path', 'tags', )

#    def clean(self):
#        cleaned_data = super(FileForm, self).clean()
#        title = cleaned_data.get('title')
##        author = cleaned_data.get('author')
##        date = cleaned_data.get('date')
#        file_path = cleaned_data.get('file_path')
#        tags = cleaned_data.get('tags')
#        if not title and not file_path and not tags:
#            raise forms.ValidationError('You have to write something!')
