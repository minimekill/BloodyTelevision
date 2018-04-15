import os
import urllib.request as req
from urllib.parse import urlparse


def download(url, to=None):
    if to:
        localfile = to
    else:
        fname = os.path.basename(urlparse(url).path)
        localfile = os.path.join('.', fname)
    print("Downloading {}".format(localfile))

    if not os.path.isfile(localfile):
        req.urlretrieve(url, localfile)

    return localfile
