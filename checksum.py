import hashlib
from dirManagement import *
from compressiontools import output

def hashFile():
    targettar = file_path(outputfolder, output)
    hashDir = file_path(outputfolder,'TarHash.txt')
    block = 65000
    file_hash = hashlib.sha256()
    with open(targettar,'rb') as f:
        blockread= f.read(block)
        while len(blockread) > 0:
            file_hash.update(blockread)
            blockread = f.read(block)
    final_digest=file_hash.hexdigest()
    with open(hashDir, 'a') as file:
        file.write(final_digest)

