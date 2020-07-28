#!/usr/bin/python3

import createrepo_c as cr
import tempfile
import urllib.request
import os

baseurl='http://downloadcontent.opensuse.org/tumbleweed/repo/oss/'

def download_file(url, target):
  urllib.request.urlretrieve(url, target)

TmpDir=tempfile.TemporaryDirectory()
download_file(baseurl + 'repodata/repomd.xml', os.path.join(TmpDir.name, "repomd.xml"))

repomd = cr.Repomd(os.path.join(TmpDir.name, 'repomd.xml'))

download_file(baseurl + repomd['appdata'].location_href, 'appdata.xml.gz')

