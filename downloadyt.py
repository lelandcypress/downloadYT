from pytube import YouTube
import os
import asyncio
ytPath = "YouTubeDownloads"
def file_path(target):
    home = os.path.expanduser('~')
    download_path = os.path.join(home, target)
    return download_path
def Download(link):
    print("Download started")
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_audio_only()
    try:
        youtubeObject.download(file_path(ytPath))
        print("Download complete")
    except:
        print("An error has occurred")
def getURLs():
    uploadpath = "C:\\Users\\soute\\Documents\\youtubeclipsforDL.txt"
    with open(uploadpath, "r") as f:
        storeYTURL = [line for line in f]
    for url in storeYTURL:
        Download(url)

if os.path.exists(ytPath):
    getURLs()
else:
    os.makedirs(file_path(ytPath))
    getURLs()


