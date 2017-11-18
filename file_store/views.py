from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    text = """<h1>TEST Bienvenue ! :)</h1>"""

    return HttpResponse(text)

def search(request):

    return render(request, 'file/search.html')

def file(request, id_fichier):

    return render(request, 'file/file.html', {'id_fichier': id_fichier})
