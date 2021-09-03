import os
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


def sendmessage(message):
    os.system(f'/usr/bin/notify-send "{message}"')
    return


image_ext = ('.jpg', '.png', '.jpeg', '.gif')
archive_ext = ('.tar.xz', '.tar.gz', '.tar.bz2', '.tar', '.zip')


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            src = str(event.src_path)
            file_name = src.split('/')[-1]
            if file_name.endswith('.crdownload') or file_name[0] == '.':
                return
            if src.endswith(('.mp3', '.wav')):
                if len(file_name) > 15:
                    name = file_name[:13] + '...'
                else:
                    name = file_name
                new_destination = f'/home/chachi/Music/{file_name}'
                sendmessage(f'{name} was moved to ~/Music')
            elif src.endswith('.deb'):
                if len(file_name) > 15:
                    name = file_name[:13] + '...'
                else:
                    name = file_name
                new_destination = f'{folder_to_track}/Deb Files/{file_name}'
                sendmessage(f'{name} was moved to Downloads/Deb Files')
            elif src.endswith(image_ext):
                if len(file_name) > 15:
                    name = file_name[:13] + '...'
                else:
                    name = file_name
                new_destination = f'/home/chachi/Pictures/{file_name}'
                sendmessage(f'{name} was moved to ~/Pictures')
            elif src.endswith(archive_ext):
                if len(file_name) > 15:
                    name = file_name[:13] + '...'
                else:
                    name = file_name
                new_destination = f'{folder_to_track}/Archives/{file_name}'
                sendmessage(f'{name} was moved to Downloads/Archives')
            else:
                if len(file_name) > 15:
                    name = file_name[:13] + '...'
                else:
                    name = file_name
                sendmessage(f"{name} was downloaded to Downloads/")
                return
            os.rename(src, new_destination)


folder_to_track = '/home/chachi/Downloads'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
# print('Observer is starting...')
observer.start()

try:
    time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
