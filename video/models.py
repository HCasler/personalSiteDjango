from django.db import models

# the original video and the manifest file and thumbnail
class Video(models.Model):
    title = models.CharField(max_length=254)
    storageLoc = models.CharField(max_length=254)
    manifestLoc = models.CharField(max_length=254)
    thumbnailLoc = models.CharField(max_length=254)

# playlist.m3u8 files
class Playlist(models.Model):
    class Playlist_Type(models.TextChoices):
        VIDEO =    "video"
        AUDIO =    "audio"
        SUBTITLE = "subti"
        IFRAMES =  "ifram"

    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    playlistType = models.CharField(max_length=5, choices=Playlist_Type.choices, default=Playlist_Type.VIDEO)
    bandwidth = models.BigIntegerField(null=True, blank=True) # empty bandwidth value allowed for audio, subtitles
    storageLoc = models.CharField(max_length=254)
    initFileLoc = models.CharField(max_length=254, blank=True) # subtitles have no init.mp4

# segment files
class MediaSegment(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    segmentNum = models.IntegerField() # I solemnly swear to never put a video with billions of segments in this app
    storageLoc = models.CharField(max_length=254)