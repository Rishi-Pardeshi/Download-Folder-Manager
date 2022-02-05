import shutil
from pathlib import Path
import os

downloads = r"C:/Users/rishi/Downloads"

fol = os.listdir(downloads)
folder = os.walk(downloads)

exe = ['.exe','.msi']
image = ['.jpg','.jpeg','.png','.gif','.jfif','.bmp']
audio = ['.mp3','.mov']
video = ['.mp4']
docs = ['.esd','.docx','.pdf','.txt']
archive = ['.zip','.tar','.7zip']

dir = []

def mainFunc(folName,file):
    if folName in fol:
        shutil.move(os.path.join(downloads,file), os.path.join(downloads,folName))
    if not folName in fol:
        os.mkdir(os.path.join(downloads,folName))
        shutil.move(os.path.join(downloads,file), os.path.join(downloads,folName))

for i in fol:
    file_extension = Path(i).suffix
    if file_extension in exe:
        mainFunc("Softwares",i)
    if file_extension in image:
        mainFunc("Images",i)
    if file_extension in audio:
        mainFunc("Audios",i)
    if file_extension in video:
        mainFunc("Videos",i)
    if file_extension in docs:
        mainFunc("Documents",i)
    if file_extension in archive:
        mainFunc("Archieves",i)
    if file_extension == '':
        dir.append(i)

if "Archieves" in dir:
    dir.remove("Archieves")
if "Documents" in dir:
    dir.remove("Documents")
if "Videos" in dir:
    dir.remove("Videos")
if "Audios" in dir:
    dir.remove("Audios")
if "Images" in dir:
    dir.remove("Images")
if "Softwares" in dir:
    dir.remove("Softwares")
if "Folders" in dir:
    dir.remove("Folders")

for fol in dir:
    shutil.move(os.path.join(downloads,fol), os.path.join(downloads,"Folders"))