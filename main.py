import os
from pathlib import Path
import shutil
from sys import path
import time
import win32com.client

# Creating shortcut file of program
current_dir = Path().resolve()
startup_folder = str(Path.home() / 'AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')
nameOfShortcut = os.path.join(startup_folder,'folder_manager.lnk')
target = os.path.join(current_dir,'main.exe')

if not os.path.isfile(nameOfShortcut):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(nameOfShortcut)
    shortcut.Targetpath = target
    shortcut.save()


l = os.listdir(current_dir)

# Getting static path of downloads folder
downloads = str(Path.home() / "Downloads")

# Creating all folder that we needed to seperate files
if not os.path.isdir(os.path.join(downloads, "Softwares")):
    os.mkdir(os.path.join(downloads,'Softwares'))

if not os.path.isdir(os.path.join(downloads, "Folders")):
    os.mkdir(os.path.join(downloads,'Folders'))

if not os.path.isdir(os.path.join(downloads, "Images")):
    os.mkdir(os.path.join(downloads,'Images'))

if not os.path.isdir(os.path.join(downloads, "Videos")):
    os.mkdir(os.path.join(downloads,'Videos'))

if not os.path.isdir(os.path.join(downloads, "Audios")):
    os.mkdir(os.path.join(downloads,'Audios'))

if not os.path.isdir(os.path.join(downloads, "Archieves")):
    os.mkdir(os.path.join(downloads,'Archieves'))

if not os.path.isdir(os.path.join(downloads, "Documents")):
    os.mkdir(os.path.join(downloads,'Documents'))

# Making array of orignal condition of download folder after sorting
orignalCon = ['Archieves', 'Audios', 'desktop.ini', 'Documents', 'Folders', 'Images', 'Softwares', 'Videos']

# Making an empty array
files = []
folders = []

# Making array for seperating different-different types of file using their extensions
exe = ['.exe', '.msi']
image = ['.jpg', '.jpeg', '.png', '.gif', '.jfif', '.bmp',
         '.tiff', '.psd', '.eps', '.ai', '.raw', '.indd']
audio = ['.mp3', '.mov', '.wav', '.pcm', '.aiff',
         '.acc', '.ogg', '.wma', '.flac', '.alac', '.']
video = ['.mp4', '.wmv', '.avi', '.avchd', '.flv',
         '.f4v', '.swf', '.mkv', '.webm', '.html5', 'mpeg-2']
docs = ['.esd', '.docx', '.pdf', '.txt', '.doc', '.html',
        '.htm', '.odt', '.xls', '.xlsx', '.ods', '.ppt', '.pptx']
archive = ['.zip', '.tar', '.7zip', '.rar', '.tar.gz']

# Making function to check if folders already present and moving files to it
def mainFunc(downloads,folName, file):
    # Checking if folder name already present
    if os.path.isdir(os.path.join(downloads, folName)):

        # Checking if file already present in path
        if os.path.isfile(os.path.join(downloads,file)) or os.path.isdir(os.path.join(downloads,file)):
            # Moving files to given folder name
            shutil.move(os.path.join(downloads, file),
                        os.path.join(downloads, folName))
        else:
            pass
    else:
        # Making directory of given folder name
        os.mkdir(os.path.join(downloads, folName))
        
        if os.path.isfile(os.path.join(downloads,file)) or os.path.isdir(os.path.join(downloads,file)):
            shutil.move(os.path.join(downloads, file),
                        os.path.join(downloads, folName))
        else:
            pass

def runMain(downloads,list):

    # Seperating files and folders from list
    for item in list:
        # getting file extension example ".exe"
        file_extension = Path(item).suffix

        # Checking for file_extension is empty, if empty it means it is a folder
        if file_extension == '':
            folders.append(item)

        # Else it will be file
        else:
            files.append(item)

    # Getting all files present in downloads folder
    for i in files:
        # Getting extension of files example ".exe"
        file_extension = Path(i).suffix
        if file_extension in exe:
            mainFunc(downloads,"Softwares", i)
        elif file_extension in image:
            mainFunc(downloads,"Images", i)
        elif file_extension in audio:
            mainFunc(downloads,"Audios", i)
        elif file_extension in video:
            mainFunc(downloads,"Videos", i)
        elif file_extension in docs:
            mainFunc(downloads,"Documents", i)
        elif file_extension in archive:
            mainFunc(downloads,"Archieves", i)
    
    # Removing main folders from folders array

    if "Softwares" in folders:
        folders.remove("Softwares")
    if "Images" in folders:
        folders.remove("Images")
    if "Archieves" in folders:
        folders.remove("Archieves")
    if "Audios" in folders:
        folders.remove("Audios")
    if "Videos" in folders:
        folders.remove("Videos")
    if "Documents" in folders:
        folders.remove("Documents")
    if "Folders" in folders:
        folders.remove("Folders")

    # Seperating folders 
    for j in folders:
        mainFunc(downloads,"Folders", j)


# runMain(downloads,list)

# Running a loop in every 5 seconds
while True:
    # Getting dynamic downloads path
    downloads = str(Path.home() / "Downloads")
    list = os.listdir(downloads)
    if not list == orignalCon:
        print("change")
        runMain(downloads,list)
    time.sleep(5)