"""
Script for making data.json
which can be loaded into the DB
"""
import sys
import json 

if len(sys.argv) < 2:
    print("Usage: generateDBdata.py -v videoTitle -cr credit -lk linkToOrig -s storagePrefix -a numAudioSegments -sub numSubtitleSegments -b bandwidth1 numSegments -b bandwidth2 numSegments")
    print("Spaces in video titles and credit must be backslash escaped")
    sys.exit()

vidTitle = None
storagePrefix = None
credit = None
link = None
numAudio = 0
audPK = None
numSubs = 0
subPK = None
bandwidths = []
videoSegs = []
vidPKs = []

for i in range(1, len(sys.argv)):
    if sys.argv[i] == '-v':
        vidTitle = sys.argv[i+1]
        i += 1 # skip the next one
    if sys.argv[i] == '-cr':
        credit = sys.argv[i+1]
        i += 1 # skip the next one
    if sys.argv[i] == '-lk':
        Link = sys.argv[i+1]
        i += 1 # skip the next one
    if sys.argv[i] == '-s':
        storagePrefix = sys.argv[i+1]
        i += 1 # skip the next one
    if sys.argv[i] == '-a':
        numAudio = int(sys.argv[i+1])
        i += 1 # skip the next one
    if sys.argv[i] == '-sub':
        numSubs = int(sys.argv[i+1])
        i += 1 # skip the next one
    if sys.argv[i] == '-b':
        bandwidths.append(sys.argv[i+1])
        videoSegs.append(int(sys.argv[i+2]))
        i += 2

jsonOut = []

playlistPK = 1

# Make video entry
vid = {
    "model": "video.Video",
    "pk": 1,
    "fields": {
        "title": vidTitle,
        "manifestLoc": "{0}/manifest.m3u8".format(storagePrefix),
        "thumbnailLoc":"{0}/thumbnail.png".format(storagePrefix),
        "credit": credit,
        "link": linkToOrig
    }
}
jsonOut.append(vid)

# put in the playlists

if numAudio > 0:
    aud = {
        "model": "video.Playlist",
        "pk": playlistPK,
        "fields": {
            "video": 1,
            "playlistType": "audio",
            "bandwidth": None,
            "storageLoc": "{0}/audio/playlist.m3u8".format(storagePrefix),
        }
    }
    jsonOut.append(aud)
    audPK = playlistPK
    playlistPK += 1

if numSubs > 0:
    sub = {
        "model": "video.Playlist",
        "pk": playlistPK,
        "fields": {
            "video": 1,
            "playlistType": "subti",
            "bandwidth": None,
            "storageLoc": "{0}/subtitles/playlist.m3u8".format(storagePrefix),
        }
    }
    jsonOut.append(sub)
    subPK = playlistPK
    playlistPK += 1

for bandwidth in bandwidths:
    vstrm = {
        "model": "video.Playlist",
        "pk": playlistPK,
        "fields": {
            "video": 1,
            "playlistType": "video",
            "bandwidth": bandwidth,
            "storageLoc": "{0}/{1}/playlist.m3u8".format(storagePrefix, bandwidth),
        }
    }
    jsonOut.append(vstrm)
    vidPKs.append(playlistPK)
    playlistPK += 1

# and now the media segments

segPK = 1

for i in range(numAudio):
    aud = {
        "model": "video.MediaSegment",
        "pk": segPK,
        "fields": {
            "playlist": audPK,
            "segmentNum": i,
            "storageLoc": "{0}/audio/seg_{1:0>2d}.ts".format(storagePrefix, i),
        }
    }
    jsonOut.append(aud)
    segPK += 1

for i in range(numSubs):
    sub = {
        "model": "video.MediaSegment",
        "pk": segPK,
        "fields": {
            "playlist": subPK,
            "segmentNum": i,
            "storageLoc": "{0}/subtitles/NASA_14225_Lucy_EGA1_Captions.en_US.vtt",
        }
    }
    jsonOut.append(sub)
    segPK += 1

for b in range(len(bandwidths)):
    bandwidth = bandwidths[b]
    segCount = videoSegs[b]
    vidPK = vidPKs[b]
    for i in range(segCount):
        vdo = {
            "model": "video.MediaSegment",
            "pk": segPK,
            "fields": {
                "playlist": vidPK,
                "segmentNum": i,
                "storageLoc": "{0}/{1}/seg_{2:0>2d}.ts".format(storagePrefix, bandwidth, i),
            }
        }
        jsonOut.append(vdo)
        segPK += 1

with open("DBdata.json", 'w') as fout:
    fout.write(json.dumps(jsonOut))
    