import os
from os import listdir
from google.cloud import storage

"""
This script creates temporary text files, uploads them to a 
Google Cloud Storage bucket, and then removes them locally.

Steps:
1. createFiles() makes N text files in the current directory.
2. addFilesToBucket() uploads them to the specified GCS bucket.
3. uploadBlobsToBucket() handles the actual upload per file.
4. removeTempFiles() cleans up local .txt files after upload.

Replace 'bucket-name' with your own bucket and ensure GCP auth.
"""


def removeTempFiles():
    listOfFiles = listdir('./')
    for file in listOfFiles:
        if isTextFile(file):
            os.remove(file)


def isTextFile(file: str) -> bool:
    return file.split('.')[-1] == 'txt'


def createFiles(numberOfFiles):
    for i in range(numberOfFiles):
        with open("file" + str(i + 1) + ".txt", "w") as file:
            file.write(str(i))




def addFilesToBucket():
    storageClient = storage.Client()
    bucket = storageClient.get_bucket('bucket-name')#Enter name of storage bucket you are looking to access

    listOfFiles = listdir('./')

    for file in listOfFiles:
        if isTextFile(file):
            uploadBlobsToBucket(bucket, file)


def uploadBlobsToBucket(bucket, file: str):
    blob = bucket.blob("test-folder/" + file)#Enter object you are looking to add to the bucket
    blob.upload_from_filename(file)

    print(f"Uploaded {file}...")


def main():
    createFiles(10)
    addFilesToBucket()
    removeTempFiles()


if __name__ == '__main__':
    main()

