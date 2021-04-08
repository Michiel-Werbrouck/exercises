#lyrics.py

import urllib.request, sys, json

artist = sys.argv[1].replace(" ", "%20")
title = sys.argv[2].replace(" ", "%20")
url = "https://api.lyrics.ovh/v1/" + artist + "/" + title

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read())
    print(data['lyrics'])