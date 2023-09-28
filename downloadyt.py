from pytube import YouTube
import os
def file_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads')
    return download_path
def Download(link):
    print("Download started")
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(file_path())
        print("Download complete")
    except:
        print("An error has occurred")


link = input("Enter the YouTube video URL: ")
Download(link)
