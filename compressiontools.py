import tarfile
from dirManagement import *
output = "CompressedYT"
def compressdir(output, source_dir):
    if not os.path.exists(file_path(outputfolder)):
        os.makedirs(file_path(outputfolder))
    output_path = os.path.join(file_path(file_path(outputfolder)), output)
    with tarfile.open(output_path, 'w:bz2') as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))