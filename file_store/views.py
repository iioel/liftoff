from django.shortcuts import render
from django.http import HttpResponse
from file_store.models import File, Tag
from django.apps import apps
from .forms import FileForm
import os, re, uuid, urllib, mimetypes, humanfriendly

# Create your views here.

def home(request):
    #text = """<h1>TEST Bienvenue ! :)</h1>"""

    #return HttpResponse(text)
    files = File.objects.all()

    return render(request, 'file/list.html', {'files': files})

def search(request):

    return render(request, 'file/search.html')

def file(request, uuid_file):
    files = File.objects.all()
    file_uuid=files.get(id=uuid.UUID(uuid_file))
    size=humanfriendly.format_size(file_uuid.file_path.size)
    return render(request, 'file/file.html', {'file': file_uuid, 'size': size})

def download(request, uuid_file):
    files = File.objects.all()
    file_uuid=files.get(id=uuid.UUID(uuid_file))
    return render(request, 'file/file.html', {'file': file_uuid})

def respond_as_attachment(request, uuid_file):
    files = File.objects.all()
    file_uuid=files.get(id=uuid.UUID(uuid_file))
    file_path = file_uuid.file_path.path
    original_filename = file_uuid.file_path.name
    dl_file = file_uuid.file_path

    #fp = open(file_path, 'rb')
    dl_file.open(mode='rb')
    response = HttpResponse(dl_file.read())
    dl_file.close()
    type, encoding = mimetypes.guess_type(original_filename)
    if type is None:
        type = 'application/octet-stream'
    response['Content-Type'] = type
    response['Content-Length'] = str(dl_file.size)
    if encoding is not None:
        response['Content-Encoding'] = encoding

    # To inspect details for the below code, see http://greenbytes.de/tech/tc2231/
    if u'WebKit' in request.META['HTTP_USER_AGENT']:
        # Safari 3.0 and Chrome 2.0 accepts UTF-8 encoded string directly.
        filename_header = 'filename=%s' % original_filename.encode('utf-8')
    elif u'MSIE' in request.META['HTTP_USER_AGENT']:
        # IE does not support internationalized filename at all.
        # It can only recognize internationalized URL, so we do the trick via routing rules.
        filename_header = ''
    else:
        # For others like Firefox, we follow RFC2231 (encoding extension in HTTP headers).
        filename_header = 'filename*=UTF-8\'\'%s' % urllib.parse.quote(original_filename.encode('utf-8'))
    response['Content-Disposition'] = 'attachment; ' + filename_header
    return response

def scan(request):
    new_filenames = os.listdir("/var/local/liftoff")
    files = File.objects.all()

    nb_filenames = len(new_filenames)
    nb_files = len(files) - 1
    nb_new = nb_filenames - nb_files    

    if request.method == 'POST':
        for new_filename in new_filenames:
            new_name = os.path.splitext(new_filename)[0]
            try:
                print("File is present with id " + str(files.get(title=new_name).id))
            except:
                new_file = File()
                new_file.title = new_name
                new_file.author = request.user
                new_file.file_path.name = new_filename
                new_file.save()
                print("New file " + new_file.title + " with id " + str(new_file.id))
        success = True
    else :
        success = False

    result = {'new':nb_new,'old':nb_files}

    return render(request, 'file/scan.html', {'success': success, 'result': result})

def modify_file(request):

    files = File.objects.all()
    untagged_files = []
    for file_ in files:
        if file_.tags.count() <= 0:
            untagged_files.append(file_)
        
    if request.method == 'POST':
        request.POST._mutable = True
        tag_list = request.POST.getlist('tags')
        for i in range(len(tag_list)) :
            if not bool(re.match(r"([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})", tag_list[i])):
                new_tag = Tag(name="%s" % tag_list[i])
                new_tag.save()
                tag_list[i] = str(new_tag.id)

        request.POST.setlist('tags', tag_list)

        form = FileForm(request.POST, request.FILES, instance=untagged_files[0])

        if form.is_valid():
            form.save()

    else:
        form = FileForm(instance=untagged_files[0])


    return render(request, 'file/modify.html', {'form': form})

def add_file(request):
    
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)

        if form.is_valid():
            new_file = form.save()
            new_file.author = request.user
            new_file.save()
            pass  # does nothing, just trigger the validation
    else:
        form = FileForm()

    return render(request, 'file/add.html', {'form': form})
