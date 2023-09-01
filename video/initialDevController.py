"""
Code for fetching video files from local static storage.
This way we cna change this logic without rewriting views.
Production implementation should have these same functions, etc.
"""
from django.core.exceptions import BadRequest
from .largeItemStorage import localStorage as DataStore

from enum import Enum
class MediaType(Enum):
    VIDEO =    "video"
    AUDIO =    "audio"
    SUBTITLE = "subti"
    IFRAMES =  "ifram"


def getVideoInfo(vidId):
    title = "Lucy Spacecraft Will Slingshot Around Earth"
    thumbUrl = "video/{0}/thumbnail".format(vidId)
    manifestUrl = "video/{0}/manifest.m3u8".format(vidId)
    return {"title": title, "thumbnail": thumbUrl, "manifest": manifestUrl}

def getManifestFile(vidId):
    pth = "videoDemoStuff/videoToUse/manifest.m3u8"
    return DataStore.getFile(pth)


def getPlaylist(vidId, mtype, bandwidth=None):
    fileData = None
    pth = None
    if mtype == MediaType.VIDEO:
        if bandwidth is None:
            raise BadRequest("Playlist of type video must specify a bandwidth")
        else:
            pth = "videoDemoStuff/videoToUse/{0}/playlist.m3u8".format(bandwidth)
    elif mtype == MediaType.AUDIO:
        pth = "videoDemoStuff/videoToUse/audio/playlist.m3u8"
    elif mtype == MediaType.SUBTITLE:
        pth = "videoDemoStuff/videoToUse/subtitles/playlist.m3u8"
    elif mtype == MediaType.IFRAMES:
        raise BadRequest("Media type {0} not implemented".format(mtype))
    else:
        raise BadRequest("Media type {0} not recognized".format(mtype))

    return DataStore.getFile(pth)


def getMediaSegment(vidId, mtype, segNum, bandwidth=None):
    pth = None
    if mtype == MediaType.VIDEO:
        if bandwidth is None:
            raise BadRequest("Playlist of type video must specify a bandwidth")
        else:
            pth = "videoDemoStuff/videoToUse/{0}/seg_{1:0>2d}.ts".format(bandwidth, segNum)
    elif mtype == MediaType.AUDIO:
        pth = "videoDemoStuff/videoToUse/audio/seg_{0:0>2d}.ts".format(segNum)
    elif mtype == MediaType.SUBTITLE:
        pth = "videoDemoStuff/videoToUse/subtitles/NASA_14225_Lucy_EGA1_Captions.en_US.vtt"
    elif mtype == MediaType.IFRAMES:
        raise BadRequest("Media type {0} not implemented".format(mtype))
    else:
        raise BadRequest("Media type {0} not recognized".format(mtype))

    return DataStore.getFileStream(pth)

def getThumbnail(vidId):
    pth = "videoDemoStuff/videoToUse/thumbnail.png"
    return DataStore.getFile(pth)

