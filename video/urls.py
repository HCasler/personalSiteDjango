from django.urls import path
from . import views

urlpatterns = [
    path("<vidId>/manifest.m3u8", views.manifest, name="manifest"),
    path("<vidId>/thumbnail", views.thumbnail, name="thumbnail"),
    path("<vidId>/<int:bandwidth>/playlist.m3u8", views.videoPlaylist, name="videoPlaylist"),
    path("<vidId>/audio/playlist.m3u8", views.audioPlaylist, name="audioPlaylist"),
    path("<vidId>/subtitles/playlist.m3u8", views.subtitlePlaylist, name="subtitlePlaylist"),

    path("<vidId>/<int:bandwidth>/seg_<int:segNum>.ts", views.videoSegment, name="videoSegment"),
    path("<vidId>/audio/seg_<int:segNum>.ts", views.audioSegment, name="audioSegment"),
    path("<vidId>/subtitles/<subName>.vtt", views.subtitleSegment, name="subtitleSegment"),
]
