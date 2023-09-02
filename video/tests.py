from django.test import TestCase
from video.models import Video, Playlist, MediaSegment, Playlist_Type
from video import DBQueries
from video import initialDevController as VideoController
from django.core.exceptions import BadRequest


class DatabaseAccessTests(TestCase):

    def setUp(self):
        # one video and one audio track
        newVid = Video.objects.create(title="Lucy Spacecraft Will Slingshot Around Earth", manifestLoc="videoDemoStuff/videoToUse/manifest.m3u8", thumbnailLoc="videoDemoStuff/videoToUse/thumbnail.png")
        self.vidPK = newVid.pk
        audPl = Playlist.objects.create(video=newVid, playlistType="audio", bandwidth=None, storageLoc="videoDemoStuff/videoToUse/audio/playlist.m3u8")
        self.astrmPK = audPl.pk
        vidPl = Playlist.objects.create(video=newVid, playlistType="video", bandwidth=1449081, storageLoc="videoDemoStuff/videoToUse/1449081/playlist.m3u8")
        self.vstrmPK = vidPl.pk
        # one segment from each
        MediaSegment.objects.create(playlist=audPl, segmentNum=0, storageLoc="videoDemoStuff/videoToUse/audio/seg_00.ts")
        MediaSegment.objects.create(playlist=vidPl, segmentNum=0, storageLoc="videoDemoStuff/videoToUse/1449081/seg_00.ts")

    def testGetVideoById(self):
        theVid = DBQueries.getVideoById(self.vidPK)
        self.assertEqual(theVid.title, "Lucy Spacecraft Will Slingshot Around Earth")

    def testGetOnePlaylistByVideoIdAndType(self):
        audPlaylist = DBQueries.getOnePlaylistByVideoIdAndType(self.vidPK, "audio")
        self.assertEqual(audPlaylist.playlistType, Playlist_Type.AUDIO)

    def testGetPlaylistByVideoTypeBandwidth(self):
        vidPlaylist = DBQueries.getPlaylistByVideoTypeBandwidth(self.vidPK, "video", 1449081)
        self.assertEqual(vidPlaylist.playlistType, Playlist_Type.VIDEO)
        self.assertEqual(vidPlaylist.bandwidth, 1449081)

    def testGetSegment(self):
        # just checks they don't fail
        DBQueries.getSegment(self.vidPK, "audio", 0)
        DBQueries.getSegment(self.vidPK, "video", 0, 1449081)


class ControllerTests(TestCase):

    def setUp(self):
        # one video and one audio track
        newVid = Video.objects.create(title="Lucy Spacecraft Will Slingshot Around Earth", manifestLoc="videoDemoStuff/videoToUse/manifest.m3u8", thumbnailLoc="videoDemoStuff/videoToUse/thumbnail.png")
        self.vidPK = newVid.pk
        audPl = Playlist.objects.create(video=newVid, playlistType="audio", bandwidth=None, storageLoc="videoDemoStuff/videoToUse/audio/playlist.m3u8")
        self.astrmPK = audPl.pk
        vidPl = Playlist.objects.create(video=newVid, playlistType="video", bandwidth=1449081, storageLoc="videoDemoStuff/videoToUse/1449081/playlist.m3u8")
        self.vstrmPK = vidPl.pk
        # one segment from each
        MediaSegment.objects.create(playlist=audPl, segmentNum=0, storageLoc="videoDemoStuff/videoToUse/audio/seg_00.ts")
        MediaSegment.objects.create(playlist=vidPl, segmentNum=0, storageLoc="videoDemoStuff/videoToUse/1449081/seg_00.ts")

    def testGetVideoInfo(self):
        vidInfo = VideoController.getVideoInfo(self.vidPK)
        self.assertEqual(vidInfo["title"], "Lucy Spacecraft Will Slingshot Around Earth")

    def testGetManifestFile(self):
        manifest = VideoController.getManifestFile(self.vidPK)
        self.assertEqual(manifest[:7], b'#EXTM3U')
        self.assertIn("#EXT-X-STREAM-INF", str(manifest))

    def testGetAudioPlaylist(self):
        playlist = VideoController.getPlaylist(self.vidPK, VideoController.MediaType.AUDIO)
        self.assertEqual(playlist[:7], b'#EXTM3U')
        self.assertIn("seg_00.ts", str(playlist))

    def testGetVideoPlaylist(self):
        playlist = VideoController.getPlaylist(self.vidPK, VideoController.MediaType.VIDEO, 1449081)
        self.assertEqual(playlist[:7], b'#EXTM3U')
        self.assertIn("seg_00.ts", str(playlist))

    def testVideoPlaylistRequiresBandwidth(self):
        try:
            playlist = VideoController.getPlaylist(self.vidPK, VideoController.MediaType.VIDEO)
            self.assertEqual(playlist, "This was supposed to raise BadRequest")
        except BadRequest:
            self.assertEqual(1, 1)
