"""file_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, re_path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^search', views.search, name='search'),
    url(r'^add', views.add_file, name='add_file'),
    url(r'^modify', views.modify_file, name='modify_file'),
    url(r'^scan', views.scan, name='scan'),
    url(r'^download/([A-Za-z0-9.]{1,})$', views.download, name='download'),
    #url(r'^[a-f0-9]{8}-([a-f0-9]{4}-){3}[a-f0-9]{12}$', views.file, name='file'),
    re_path(r'([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})$', views.file, name='file'),
    re_path(r'([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})/download$', views.respond_as_attachment, name='file_dl'),
    #url(r'^(?P<uuid>\[a-f0-9]{8}-([a-f0-9]{4}-){3}[a-f0-9]{12})$', views.file, name='file'),
]
