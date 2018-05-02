#!/usr/bin/python

import re
import sys

APPDATA="appdata.html"
APPCNT = open(APPDATA, 'r').read()
DATA = re.findall('<tr><td class="alt">Keywords</td><td>(\d+)/(\d+)</td><td class="thin">.*</td></tr>', APPCNT)

print ("%s:%s" % (sys.argv[1], DATA[0][1]))

