#!/bin/bash


pushd /home/dimstar/src/gs-stats.o.o/appstream-trend/
git pull

SNAPSHOT=$(python3 get-snapshot-version.py)

# Update data.txt
cp data.txt data.txt.tmp
rm -f appdata.html.xz appdata.xml.gz appdata-failed.xml.gz
python3 download-appdata.py
appstream-util status-html appdata.xml.gz appdata.html
appstream-util matrix-html appdata.xml.gz matrix-view.html
#appstream-util status-html appdata-failed.xml.gz appdata-failed.html

python update-stats.py $SNAPSHOT >> data.txt.tmp

# Remove duplicate entries from data.txt
uniq data.txt.tmp > data.txt
rm data.txt.tmp

# Update the .html files in git for reference
./update-appdata_html.sh $SNAPSHOT

