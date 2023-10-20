from dirManagement import *
def generateUploadScript():
    ouput_dirmanfilename= "dirManagement.py"
    ouput_mainfilename= "main.py"
    ouput_runchecksumfilename= "runchecksum.py"
    ouput_runUpload= "runUpload.py"


    dirmancontent="""
import os
tarFile = "CompressedYT"
checksumFile = "TarHash.txt"
    
def file_path(targetDir,*file):
    home = os.path.expanduser('~')
    if file:
        download_path = os.path.join(home, targetDir, *file)
    else:
        download_path = os.path.join(home, targetDir)
    return download_path"""

    maincontent ="""
import hashlib
from runUpload import *
from runchecksum import *
if __name__ == '__main__':
    if runCheckSum():
        findDir()
else:
    print("Checksum failed")
    exit()
    """
    checksumcontent ="""
import hashlib
from dirManagement import tarFile, checksumFile
def runCheckSum():
    block = 65000
    file_hash = hashlib.sha256()
    with open(tarFile,'rb') as f:
        blockread= f.read(block)
        while len(blockread) > 0:
            file_hash.update(blockread)
            blockread = f.read(block)
    final_digest = file_hash.hexdigest()
    try:
        with open(checksumFile, 'r') as f:
            YTChecksum = f.read()
            if final_digest == YTChecksum:
                return True
    except Exception as e:
        exit(e)
    """

    runUploadcontent ="""    
import tarfile
from dirManagement import tarFile
import os
from datetime import datetime
import shutil
today = datetime.today()
year = today.strftime('%Y')
month = today.strftime('%m')
day = today.strftime('%d')
orgYTFolder = "YouTubeDownloads"
#starts with decompressing TAR files in target directory

#checks for videos directory to verify we are in the correct node
def findDir():
    if os.path.exists("videos"):
        decompressVids()
    else:
        print("Video Folder not found")

def decompressVids():
    with tarfile.open(tarFile, 'r:bz2')as tar:
        tar.extractall()
        tar.close()
    moveFiles()

# Verifies files are placed in the correct file path. YouTube node makes use of a YYYY/MM/DD folder hierarchy.
# This script creates this hierachy based on the current date.
def moveFiles():
    basedir = "videos"
    todaysDate = [year,month,day]
    for component in todaysDate:
        sourcedir = os.path.join(basedir,component)
        if not os.path.exists(sourcedir):
            os.makedirs(sourcedir)
        basedir = sourcedir

    for video in os.listdir(orgYTFolder):
        sourceVid = os.path.join(orgYTFolder,video)
        finalDestination = os.path.join(basedir, video)
        shutil.move(sourceVid ,finalDestination)
    """

    file_dict={
    ouput_dirmanfilename: dirmancontent,
    ouput_mainfilename : maincontent,
    ouput_runchecksumfilename : checksumcontent,
    ouput_runUpload : runUploadcontent
    }
    for fname,content in file_dict.items():
        payloadFolder = file_path(outputfolder,fname)
        with open(payloadFolder, "w") as output_file:
            output_file.write(content)
