"""
Code for fetching video files from local static storage.
This way we cna change this logic without rewriting views.
Production implementation should have these same functions, etc.
"""
from django.core.exceptions import BadRequest
from .largeItemStorage import localStorage as DataStore
from . import DBQueries

import logging
logger = logging.getLogger(__name__)

from enum import Enum
class MediaType(Enum):
    VIDEO =    "video"
    AUDIO =    "audio"
    SUBTITLE = "subti"
    IFRAMES =  "ifram"


def getVideoInfo(vidId):
    theVid = DBQueries.getVideoById(vidId)
    thumbUrl = "video/{0}/thumbnail".format(vidId)
    manifestUrl = "video/{0}/manifest.m3u8".format(vidId)
    outDict = {"title": theVid.title, "thumbnail": thumbUrl, "manifest": manifestUrl, "credit": theVid.credit, "url": theVid.link, "id": theVid.pk}
    logger.debug(outDict)
    return outDict

def getTopVideoInfo():
    return getVideoInfo(1)

def getManifestFile(vidId):
    logger.debug("received request for video id {0} manifest".format(vidId))
    theVid = DBQueries.getVideoById(vidId)
    return DataStore.getFile(theVid.manifestLoc)


def getPlaylist(vidId, mtype, bandwidth=None):
    logger.debug("received request for video id {0}, playlist type {1}, bandwidth {2}".format(vidId, mtype, bandwidth))
    fileData = None
    playlist = None
    if mtype == MediaType.VIDEO:
        if bandwidth is None:
            raise BadRequest("Playlist of type video must specify a bandwidth")
        else:
            playlist = DBQueries.getPlaylistByVideoTypeBandwidth(vidId, mtype.value, bandwidth)
    elif mtype == MediaType.IFRAMES:
        raise BadRequest("Media type {0} not implemented".format(mtype))
    elif mtype == MediaType.AUDIO or mtype == MediaType.SUBTITLE:
        playlist = DBQueries.getOnePlaylistByVideoIdAndType(vidId, mtype.value)
    else:
        raise BadRequest("Media type {0} not recognized".format(mtype))

    return DataStore.getFile(playlist.storageLoc)


def getMediaSegment(vidId, mtype, segNum, bandwidth=None):
    logger.debug("received request for video id {0}, playlist type {1}, bandwidth {2}, segment number {3}".format(vidId, mtype, bandwidth, segNum))
    segment = None
    if mtype == MediaType.VIDEO:
        if bandwidth is None:
            raise BadRequest("Playlist of type video must specify a bandwidth")
        else:
            segment = DBQueries.getSegment(vidId, mtype.value, segNum, bandwidth)
    elif mtype == MediaType.AUDIO or mtype == MediaType.SUBTITLE:
        segment = DBQueries.getSegment(vidId, mtype.value, segNum)
    elif mtype == MediaType.IFRAMES:
        raise BadRequest("Media type {0} not implemented".format(mtype))
    else:
        raise BadRequest("Media type {0} not recognized".format(mtype))

    logger.debug("storage location: {0}".format(segment.storageLoc))
    return DataStore.getFileStream(segment.storageLoc)

def getSubtitles(vidId):
    logger.debug("received request for video id {0} subtitles".format(vidId))
    segment = DBQueries. getSubtitles(vidId)
    logger.debug("storage location: {0}".format(segment.storageLoc))
    return DataStore.getFile(segment.storageLoc)

def getThumbnail(vidId):
    theVid = DBQueries.getVideoById(vidId)
    return DataStore.getFile(theVid.thumbnailLoc)

