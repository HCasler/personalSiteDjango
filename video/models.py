from django.db import models

class Playlist_Type(models.TextChoices):
    VIDEO =    "video"
    AUDIO =    "audio"
    SUBTITLE = "subti"
    IFRAMES =  "ifram"

# the original video and the manifest file and thumbnail
class Video(models.Model):
    def __str__(self):
        return "Video {0}: {1}".format(self.pk, self.title)

    title = models.CharField(max_length=254)
    manifestLoc = models.CharField(max_length=254)
    thumbnailLoc = models.CharField(max_length=254)
    credit  = models.CharField(max_length=254)
    link = models.CharField(max_length=254)

# playlist.m3u8 files
class Playlist(models.Model):

    def __str__(self):
        if self.playlistType == Playlist_Type.VIDEO:
            return "Video {0}: {1} playlist id {2}, bandwidth {3}".format(self.video.pk, self.playlistType, self.id, self.bandwidth)
        else:
            return "Video {0}: {1} playlist id {2}".format(self.video.pk, self.playlistType, self.id)

    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    playlistType = models.CharField(max_length=5, choices=Playlist_Type.choices, default=Playlist_Type.VIDEO)
    bandwidth = models.BigIntegerField(null=True, blank=True) # empty bandwidth value allowed for audio, subtitles
    storageLoc = models.CharField(max_length=254)

# segment files
class MediaSegment(models.Model):
    def __str__(self):
        return "Media segment {0} from playlist id {1}".format(self.segmentNum, self.playlist.pk)

    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    segmentNum = models.IntegerField() # I solemnly swear to never put a video with billions of segments in this app
    storageLoc = models.CharField(max_length=254)