from downloadyt import *

if __name__ == "__main__":
    if os.path.exists(ytPath):
        init()
    else:
        os.makedirs(file_path(ytPath))
        print("Youtube download directory not found! Creating folder at "+file_path(ytPath))
        init()
