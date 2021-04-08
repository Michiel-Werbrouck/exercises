# download.py

import urllib.request, sys

with urllib.request.urlopen(sys.argv[1]) as response:
    webContent = response.read()
    print(webContent)