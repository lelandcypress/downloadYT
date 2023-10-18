import os
import glob
ytPath = "YouTubeDownloads"
outputfolder = "CompressedYT"
def file_path(targetDir,*file):
    home = os.path.expanduser('~')
    if file:
        download_path = os.path.join(home, targetDir, *file)
    else:
        download_path = os.path.join(home, targetDir)
    return download_path

def cleanup(dir):
    dir = glob.glob(dir+'\\*.mp4')
    for files in dir:
        os.remove(files)

