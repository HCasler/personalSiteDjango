from django.urls import path
from . import views

urlpatterns = [
    path("<vidId>/manifest.m3u8", views.manifest, name="manifest"),
    path("<vidId>/<int:bandwidth>/playlist.m3u8", views.videoPlaylist, name="videoPlaylist"),
    path("<vidId>/audio/playlist.m3u8", views.audioPlaylist, name="audioPlaylist"),
    path("<vidId>/<int:bandwidth>/init.mp4", views.videoInit, name="videoInit"),
    path("<vidId>/<int:bandwidth>/seg-<int:segNum>.ts", views.videoSegment, name="videoSegment"),
    path("<vidId>/audio/init.mp4", views.audioInit, name="audioInit"),
    path("<vidId>/audio/seg-<int:segNum>.ts", views.audioSegment, name="audioSegment"),
]
