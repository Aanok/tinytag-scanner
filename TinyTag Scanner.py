import os.path, Media
from tinytag import TinyTag

supported_containers = [
    '.mp3',
    '.ogg',
    '.opus',
    '.mp4',
    '.m4a',
    '.flac',
    '.wma',
    '.wav'
]


def utf8(string):
    return string.encode('utf-8') if string else None


def Scan(path, files, mediaList, subdirs, language=None, root=None):
    for f in files:
        filename, extension = os.path.splitext(f)
        if extension not in supported_containers:
            continue

        tags = TinyTag.get(f)
        plex_track = Media.Track(
            artist          =   utf8(tags.artist),
            album           =   utf8(tags.album),
            title           =   utf8(tags.title),
            index           =   utf8(tags.track),
            year            =   utf8(tags.year),
            disc            =   utf8(tags.disc),
            album_artist    =   utf8(tags.albumartist)
        )
	plex_track.parts.append(f)
	mediaList.append(plex_track)
