"""
DB access code
Keep it out of controller logic code
"""
from .models import Video, Playlist, MediaSegment
import logging

logger = logging.getLogger(__name__)

def getVideoById(vidId):
    # select * from video_video where id = vidId
    oneVid = Video.objects.get(pk=vidId)
    return oneVid

def getOnePlaylistByVideoIdAndType(vidId, mtype):
    # select * from video_playlist where video_id = vidId and playlistType = mtype
    playlist = Playlist.objects.get(video_id=vidId, playlistType=mtype)
    return playlist

def getPlaylistByVideoTypeBandwidth(vidId, mtype, vbandwidth):
    # select * from video_playlist where video_id = vidId and playlistType = mtype and bandwidth=vbandwidth
    playlist = Playlist.objects.get(video_id=vidId, playlistType=mtype, bandwidth=vbandwidth)
    return playlist

def getSegment(vidId, mtype, segNum, bandwidth=None):
    segment = None
    if bandwidth is None:
        # select * from video_mediasegment m join video_playlist p
        # on p.id = m.playlist_id 
        # where p.video_id = vidId and p.playlistType = mtype and m.segmentNum = 5
        segment = MediaSegment.objects.get(playlist__video_id=vidId, playlist__playlistType=mtype, segmentNum=segNum)
    else:
        segment = MediaSegment.objects.get(playlist__video_id=vidId, playlist__playlistType=mtype, playlist__bandwidth=bandwidth, segmentNum=segNum)
    return segment
