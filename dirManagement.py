import os
import glob
ytPath = "YouTubeDownloads"
outputfolder = "CompressedYT"
def file_path(target):
    home = os.path.expanduser('~')
    download_path = os.path.join(home, target)
    return download_path

def cleanup(dir):
    dir = glob.glob(dir+'\\*.mp4')
    for files in dir:
        os.remove(files)

