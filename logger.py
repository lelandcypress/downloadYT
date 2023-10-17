import os
from datetime import datetime
from dirManagement import file_path
logpath ='CompressedYT\\Download Logs'
logdate = datetime.today().strftime('%Y-%m-%d')
logfilename= f"DownloadLog{logdate}.txt"
logdir = file_path(logpath)
logTarget = os.path.join(logdir,logfilename)
def logYTDL(arr):
    if not os.path.exists(logdir):
        os.makedirs(logdir)
    for link in arr:
        with open(logTarget, 'a') as file:
            file.write(link)



