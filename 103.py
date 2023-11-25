import time 
import os
import shutil
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(event)

    event_handler = FileMovementHandler()

    observer = Observer()

    observer.schedule(event_handler,from_dir,recursive = True)
    observer.start()

    try:
        while True:
            time.sleep(2)
            print("running")
    except KeyboardInterrupt:
        print("stopped")
        observer.stop()