"""
Getting files from Azure Storage
"""
from django.conf import settings
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# returns bytes
def getFile(location):
    blobServiceClient = BlobServiceClient.from_connection_string(settings.AZURE_STORAGE_CONNECTION_STRING)
    containerClient = blobServiceClient.get_container_client(container=settings.VIDEO_STORAGE_CONTAINER)
    outData = containerClient.download_blob(location).readall()
    return outData

# returns an iterable of data
def getFileStream(location):
    blobServiceClient = BlobServiceClient.from_connection_string(settings.AZURE_STORAGE_CONNECTION_STRING)
    containerClient = blobServiceClient.get_container_client(container=settings.VIDEO_STORAGE_CONTAINER)
    return containerClient.download_blob(location).chunks()