"""
Code for fetching local files, for local dev purposes
"""
from django.conf import settings

def getFile(location):
    fullPath = settings.STORAGE_BASE + "/{0}".format(location)
    with open(fullPath, 'rb') as f:
        fileData = f.read()
    return fileData

def getFileStream(location):
    fullPath = settings.STORAGE_BASE + "/{0}".format(location)
    return open(fullPath, 'rb')

