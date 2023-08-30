"""
Code for fetching video files from local static storage.
This way we cna change this logic without rewriting views.
Production implementation should have these same functions, etc.
"""
from django.core.exceptions import BadRequest

from enum import Enum
class MediaType(Enum):
    VIDEO =    "video"
    AUDIO =    "audio"
    SUBTITLE = "subti"
    IFRAMES =  "ifram"


def getManifestFile(vidId):
    fileData = None
    with open('video/static/video/sampleManifest.m3u8') as f:
        fileData = f.read()
    return fileData


def getPlaylist(vidId, mtype, bandwidth=None):
    fileData = None
    localFile = None
    if mtype == MediaType.VIDEO:
        if bandwidth is None:
            raise BadRequest("Playlist of type video must specify a bandwidth")
        else:
            localFile = 'video/static/video/sampleVideoPlaylist.m3u8'
    elif mtype == MediaType.AUDIO:
        localFile = 'video/static/video/sampleAudioPlaylist.m3u8'
    elif mtype == MediaType.SUBTITLE or mtype == MediaType.IFRAMES:
        raise BadRequest("Media type {0} not implemented".format(mtype))
    else:
        raise BadRequest("Media type {0} not recognized".format(mtype))

    with open(localFile) as f:
        fileData = f.read()
    return fileData


def getInitFile(vidId, mtype, bandwidth=None):
    fileData = None
    localFile = None
    if mtype == MediaType.VIDEO:
        if bandwidth is None:
            raise BadRequest("Playlist of type video must specify a bandwidth")
        else:
            return "TODO: video init"
    elif mtype == MediaType.AUDIO:
        return "TODO: audio init"
    elif mtype == MediaType.SUBTITLE or mtype == MediaType.IFRAMES:
        raise BadRequest("Media type {0} does not use init files".format(mtype))
    else:
        raise BadRequest("Media type {0} not recognized".format(mtype))


def getMediaSegment(vidId, mtype, segNum, bandwidth=None):
    fileData = None
    localFile = None
    if mtype == MediaType.VIDEO:
        if bandwidth is None:
            raise BadRequest("Playlist of type video must specify a bandwidth")
        else:
            return "TODO: video segment {0}".format(segNum)
    elif mtype == MediaType.AUDIO:
        return "TODO: audio segment {0}".format(segNum)
    elif mtype == MediaType.SUBTITLE or mtype == MediaType.IFRAMES:
        raise BadRequest("Media type {0} does not use init files".format(mtype))
    else:
        raise BadRequest("Media type {0} not recognized".format(mtype))
