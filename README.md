The main feature of this scanner and reason I wrote it is that it can parse Opus files, which Plex's default scanner cannot, for some reason.

# Disclaimer
This script is meant for my own personal use only. It is extremely fragile and naive, so I do not guarantee it will work under any circumstance.

# Installation (Linux only)
1. Grab [tinytag.py](https://github.com/devsnd/tinytag/blob/master/tinytag/tinytag.py) from upstream and place it in `/usr/lib//usr/lib/plexmediaserver/Resources/Plug-ins-fd05be322/Scanners.bundle/Contents/Resources/Common`.
1. Put `TinyTag Scanner.py` in `/usr/lib//usr/lib/plexmediaserver/Resources/Plug-ins-fd05be322/Scanners.bundle/Contents/Resources/Music`.
1. Reboot PMS (restart the service). The scanner should now be available for Music Libraries.

I imagine the process to be similar for Windows and OS X, just with different folders.
