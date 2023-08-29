from django.shortcuts import render
import logging

# TEMPORARY, will replace with real storage
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def manifest(request, vidName):
    # TODO: vidName used to find an object in the DB, pointing to which manifest file to return
    # manifest file then pulled out of storage
    fileData = None
    with open('video/static/video/sampleManifest.m3u8') as f:
        fileData = f.read()
    resp = HttpResponse(fileData)
    resp.headers["Content-Type"] = "application/vnd.apple.mpegurl"
    return resp

def videoPlaylist(request, vidName, bandwidth):
    # TODO: vidName and bandwidth used to find an object in the DB, pointing to which playlist to return
    # playlist file then pulled out of storage
    fileData = None
    with open('video/static/video/sampleVideoPlaylist.m3u8') as f:
        fileData = f.read()
    resp = HttpResponse(fileData)
    resp.headers["Content-Type"] = "application/vnd.apple.mpegurl"
    return resp

def audioPlaylist(request, vidName):
    # TODO: vidName and bandwidth used to find an object in the DB, pointing to which playlist to return
    # playlist file then pulled out of storage
    fileData = None
    with open('video/static/video/sampleAudioPlaylist.m3u8') as f:
        fileData = f.read()
    resp = HttpResponse(fileData)
    resp.headers["Content-Type"] = "application/vnd.apple.mpegurl"
    return resp

def videoInit(request, vidName, bandwidth):
    # TODO: vidName and bandwidth used to find an object in the DB, pointing to which init file to return
    # init file then pulled out of storage
    resp = HttpResponse("TODO: video init")
    resp.headers["Content-Type"] = "video/mp4"
    return resp

def videoSegment(request, vidName, bandwidth, segNum):
    # TODO: get DB data, pull from storage, you know
    resp = HttpResponse("TODO: video segment {0}".format(segNum))
    resp.headers["Content-Type"] = "video/mp2t"
    return resp

def audioInit(request, vidName):
    # TODO: vidName used to find an object in the DB, pointing to which init file to return
    # init file then pulled out of storage
    resp = HttpResponse("TODO: audio init")
    resp.headers["Content-Type"] = "video/mp4"
    return resp

def audioSegment(request, vidName, segNum):
    # TODO: get DB data, pull from storage, you know
    resp = HttpResponse("TODO: audio segment {0}".format(segNum))
    resp.headers["Content-Type"] = "video/mp2t"
    return resp