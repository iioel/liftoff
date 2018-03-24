from django.shortcuts import render
from django.http import HttpResponse
from file_store.models import File

# Create your views here.

files = File.objects.all()

def home(request):
    #text = """<h1>TEST Bienvenue ! :)</h1>"""

    #return HttpResponse(text)

    return render(request, 'file/list.html', {'files': files})

def search(request):

    return render(request, 'file/search.html')

def file(request):

    return render(request, 'file/file.html')
