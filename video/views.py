from django.http import HttpResponse
import logging

# TODO: replace this import with the "proper" version for deployment
from . import initialDevController as VideoController

logger = logging.getLogger(__name__)

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

def videoInit(request, vidId, bandwidth):
    fileData = VideoController.getInitFile(vidId, VideoController.MediaType.VIDEO, bandwidth)
    resp = HttpResponse(fileData)
    resp.headers["Content-Type"] = "video/mp4"
    return resp

def videoSegment(request, vidId, bandwidth, segNum):
    fileData = VideoController.getMediaSegment(vidId, VideoController.MediaType.VIDEO, segNum, bandwidth)
    resp = HttpResponse(fileData)
    resp.headers["Content-Type"] = "video/mp2t"
    return resp

def audioInit(request, vidId):
    fileData = VideoController.getInitFile(vidId, VideoController.MediaType.AUDIO, bandwidth=None)
    resp = HttpResponse(fileData)
    resp.headers["Content-Type"] = "video/mp4"
    return resp

def audioSegment(request, vidId, segNum):
    fileData = VideoController.getMediaSegment(vidId, VideoController.MediaType.AUDIO, segNum, bandwidth=None)
    resp = HttpResponse(fileData)
    resp.headers["Content-Type"] = "video/mp2t"
    return resp