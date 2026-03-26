#!/usr/bin/python3

import re
import sys

APPDATA="appdata.html"
with open(APPDATA, 'r') as f:
    APPCNT = f.read()
DATA = re.findall(r'<tr><td class="alt">Keywords</td><td>(\d+)/(\d+)</td><td class="thin">.*</td></tr>', APPCNT)

print ("%s:%s" % (sys.argv[1], DATA[0][1]))

