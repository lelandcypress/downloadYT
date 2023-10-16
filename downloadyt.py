from pytube import YouTube
import os
ytPath = "YouTubeDownloads"
def file_path(target):
    home = os.path.expanduser('~')
    download_path = os.path.join(home, target)
    return download_path
def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_audio_only()
    youtubeObject.download(file_path(ytPath))
    print("An error has occurred")
def startDownload():
    uploadfolder = "Documents\\youtubeclipsforDL.txt"
    i = 1
    with open(file_path(uploadfolder), "r") as f:
        storeYTURL = [line for line in f]
    print(f"{len(storeYTURL)} Links in file...download staring")
    try:
        for url in storeYTURL:
            print(f"Downloading {i} of {len(storeYTURL)}")
            Download(url)
            i += 1
    except: print("Error with download")
    print("Script complete!")


