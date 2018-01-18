from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from landing.models import Event, Photos, Videos

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Event.objects.all().order_by("-date")[:3],
    		template_name="landing/home.html")),
    url(r'^photos/$', ListView.as_view(queryset=Photos.objects.all().order_by("-date"),
    		template_name="landing/photos.html")),
    url(r'^videos/$', ListView.as_view(queryset=Videos.objects.all().order_by("-date"),
    		template_name="landing/videos.html")),
]