from downloadyt import *
from compress import *

if __name__ == "__main__":
    if os.path.exists(ytPath):
        startDownload()
    else:
        os.makedirs(file_path(ytPath))
        print(f"Youtube download directory not found! Creating folder at {file_path(ytPath)}")
        startDownload()
    #if os.path.exists(file_path("Documents\\youtubeclipsforDL.txt")):
        #print("YIPPEEE")

