from pytube import YouTube
from compressiontools import *
from dirManagement import *
from logger import *
from checksum import *
from generateScript import generateUploadScript
storeYTURL= []
def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    youtubeObject.download(file_path(ytPath))
def startDownload():
    uploadfolder = "Documents\\youtubeclipsforDL.txt"
    i = 1
    with open(file_path(uploadfolder), "r") as f:
        storeYTURL = [line for line in f]
    print(f"{len(storeYTURL)} links in file...download starting")
    for url in storeYTURL:
        try:
            print(f"Downloading {i} of {len(storeYTURL)}")
            Download(url)
            i += 1
        except Exception as e:
            print(e)
            continue
    print("Compressing....")
    compressdir(output, file_path(ytPath))
    print("Compression complete!")
    print("Logging")
    logYTDL(storeYTURL)
    print("Logging Complete")
    print("Hashing")
    hashFile()
    print("Hash complete")
    print("Generating upload script")
    generateUploadScript()
    delete = input("Would you like to delete the MP4s now? y/n: ")
    if delete == 'y' or delete =='Y':
        print("Removing MP4s from YTDownloads!")
        cleanup(file_path(ytPath))
        print("Files deleted!\nScript Complete")
    elif delete == 'n' or 'N':
        print("Exiting Script!")
        exit()

