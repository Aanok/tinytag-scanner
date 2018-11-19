import re, os.path, Media
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


# Unicode control characters can appear in ID3v2 tags but are not legal in XML.
RE_UNICODE_CONTROL =  u'([\u0000-\u0008\u000b-\u000c\u000e-\u001f\ufffe-\uffff])' + \
                      u'|' + \
                      u'([%s-%s][^%s-%s])|([^%s-%s][%s-%s])|([%s-%s]$)|(^[%s-%s])' % \
                      (
                        unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),
                        unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),
                        unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff)
                      )


def utf8(string):
    try:
        string = re.sub(RE_UNICODE_CONTROL, '', string.strip().encode('utf-8'))
    except:
        pass
    return string


def Scan(path, files, mediaList, subdirs, language=None, root=None):
    for f in files:
        filename, extension = os.path.splitext(f)
        if extension not in supported_containers:
            continue

        tags = TinyTag.get(f)
        plex_track = Media.Track(
            artist          =   utf8(tags.artist) or '[Unknown Artist]',
            album           =   utf8(tags.album) or '[Unkown Album]',
            title           =   utf8(tags.title) or os.path.basename(filename),
            index           =   utf8(tags.track),
            year            =   utf8(tags.year),
            disc            =   utf8(tags.disc),
            album_artist    =   utf8(tags.albumartist)
        )
	plex_track.parts.append(f)
	mediaList.append(plex_track)
