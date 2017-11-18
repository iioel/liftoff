from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    text = """<h1>TEST Bienvenue ! :)</h1>"""

    return HttpResponse(text)

def search(request):
    text = """<h1>Page de recherche</h1>
              <p>Ici, il sera possible de rechercher des fichiers"""

    return HttpResponse(text)

def file(request, id_fichier):
    text = """<h1>Page de consultation de fichier</h1>
              <p>Vous avez demandé le fichier {0}""".format(id_fichier)

    return HttpResponse(text)
