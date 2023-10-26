#!/usr/bin/python3

import urllib.request
import re

CONTENT="http://download.opensuse.org/tumbleweed/repo/oss/media.1/media"
APPDATA="http://download.opensuse.org/tumbleweed/repo/oss/suse/setup/descr/appdata.html"

CNT = urllib.request.urlopen(CONTENT).read().decode('utf-8')
DISTRO = re.findall("openSUSE-(........)-x86_64-Build.*", CNT)

V1 = DISTRO[0]
SNAPDATE=V1[:4] + '-' + V1[4:6] + '-' + V1[6:]

print (SNAPDATE)
