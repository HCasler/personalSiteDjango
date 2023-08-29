from django.urls import path
from . import views

urlpatterns = [
    path("<vidName>/manifest.m3u8", views.manifest, name="manifest"),
    path("<vidName>/<int:bandwidth>/playlist.m3u8", views.videoPlaylist, name="videoPlaylist"),
    path("<vidName>/audio/playlist.m3u8", views.audioPlaylist, name="audioPlaylist"),
    path("<vidName>/<int:bandwidth>/init.mp4", views.videoInit, name="videoInit"),
    path("<vidName>/<int:bandwidth>/seg-<int:segNum>.ts", views.videoSegment, name="videoSegment"),
    path("<vidName>/audio/init.mp4", views.audioInit, name="audioInit"),
    path("<vidName>/audio/seg-<int:segNum>.ts", views.audioSegment, name="audioSegment"),
]
