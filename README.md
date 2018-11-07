The main feature of this scanner and reason I wrote it is that it can parse Opus files, which Plex's default scanner cannot, for some reason.

# Disclaimer
This script is meant for my own personal use only. It is extremely fragile and naive, so I do not guarantee it will work under any circumstance.

# Installation (Linux only)
Assuming Plex is installed in the default directory `/var/lib/plexmediaserver/` and that it is run by user `plex`, then you may execute
```
cd "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/"
sudo mkdir -p "Scanners/Common Scanners/Music"
sudo wget 'https://raw.githubusercontent.com/devsnd/tinytag/master/tinytag/tinytag.py' -o Scanners/Common/tinytag.py
sudo wget 'https://raw.githubusercontent.com/Aanok/tinytag-scanner/master/TinyTag%20Scanner.py' -o Scanners/Music/TinyTag\ Scanner.py
sudo chown -R plex:plex Scanners
```
See [this](https://forums.plex.tv/t/how-to-install-a-custom-scanner/5960) forum post for more information on Windows and OS X.
