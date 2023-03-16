from tkinter.filedialog import askdirectory
from tkinter import Tk
import os , hashlib
from pathlib import Path
Tk().withdraw()

path =  askdirectory(title="Select DATABASE folder")

file_list = os.walk(path)

unique = dict()

hashfile_list = []


for root,folders,files in file_list:
    for file in files:
        path = Path(os.path.join(root,file))
        # MD5 in action below
        fileHash = hashlib.md5(open(path,'rb').read()).hexdigest()   
        print(fileHash)
        hashfile_list.append(fileHash)

print(hashfile_list) # The Data set is defined and is ready to get searched

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


scannedfolder =  askdirectory(title="Select a folder containing DOCUMENT")
file_list = os.walk(scannedfolder)
unique = dict()

for root,folders,files in file_list:
    for file in files:
        scannedfolder = Path(os.path.join(root,file))
        # MD5 in action below
        fileHash = hashlib.md5(open(scannedfolder,'rb').read()).hexdigest()   
        print(fileHash)
        photokey = fileHash

if photokey in hashfile_list:
    print("\n\n** AUTHORIZED **")
else:
    print("\n\n ** UN AUTHORIZED **")
