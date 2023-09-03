from django.http import HttpResponse, FileResponse
import logging
import json

# TODO: replace this import with the "proper" version for deployment
from . import initialDevController as VideoController

logger = logging.getLogger(__name__)

def topVideoInfo(request):
    vidInfo = VideoController.getTopVideoInfo()
    resp = HttpResponse(json.dumps(vidInfo))
    resp.headers["Content-Type"] = "application/json"
    return resp


def manifest(request, vidId):
    fileData = VideoController.getManifestFile(vidId)
    resp = HttpResponse(fileData)
    resp.headers["Content-Type"] = "application/vnd.apple.mpegurl"
    return resp

def videoPlaylist(request, vidId, bandwidth):
    fileData = VideoController.getPlaylist(vidId, VideoController.MediaType.VIDEO, bandwidth)
    resp = HttpResponse(fileData)
    resp.headers["Content-Type"] = "application/vnd.apple.mpegurl"
    return resp

def audioPlaylist(request, vidId):
    fileData = VideoController.getPlaylist(vidId, VideoController.MediaType.AUDIO, bandwidth=None)
    resp = HttpResponse(fileData)
    resp.headers["Content-Type"] = "application/vnd.apple.mpegurl"
    return resp

def subtitlePlaylist(request, vidId):
    fileData = VideoController.getPlaylist(vidId, VideoController.MediaType.SUBTITLE, bandwidth=None)
    resp = HttpResponse(fileData)
    resp.headers["Content-Type"] = "application/vnd.apple.mpegurl"
    return resp

def videoSegment(request, vidId, bandwidth, segNum):
    resp = FileResponse(VideoController.getMediaSegment(vidId, VideoController.MediaType.VIDEO, segNum, bandwidth))
    resp.headers["Content-Type"] = "video/mp2t"
    return resp

def audioSegment(request, vidId, segNum):
    resp = FileResponse(VideoController.getMediaSegment(vidId, VideoController.MediaType.AUDIO, segNum, bandwidth=None))
    resp.headers["Content-Type"] = "video/mp2t"
    return resp

def subtitleSegment(request, vidId, subName):
    resp = FileResponse(VideoController.getMediaSegment(vidId, VideoController.MediaType.SUBTITLE, subName, bandwidth=None))
    resp.headers["Content-Type"] = "text/vtt"
    return resp

def thumbnail(request, vidId):
    fileData = VideoController.getThumbnail(vidId)
    resp = HttpResponse(fileData)
    resp.headers["Content-Type"] = "image/png"
    return resp
