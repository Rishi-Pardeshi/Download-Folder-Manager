import os
current_dir = Path().resolve()
startup_folder = str(Path.home() / 'AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')

# Running a loop in every 5 seconds
while True:
    # Getting dynamic downloads path
    downloads = str(Path.home() / "Downloads")
    list = os.listdir(downloads)
    if not list == orignalCon:
        print("change")
        runMain(downloads,list)
    time.sleep(5)