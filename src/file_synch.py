import os
import shutil
import time
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class EventHandler(FileSystemEventHandler):
    def __init__(self, log_file):
        self.log_file = log_file
        self.__set_logger()

    def on_created(self, event) -> None:
        if event.is_directory:
            return
        else:
            logging.info(f"File created: {event.src_path}")

    def on_deleted(self, event) -> None:
        if event.is_directory:
            return
        else:
            logging.info(f"File deleted: {event.src_path}")

    def on_moved(self, event) -> None:
        logging.info(f"Moved {event.src_path} to {event.dest_path}")

    def __set_logger(self):
        logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(message)s',
                handlers=[
                    logging.FileHandler(self.log_file),
                    logging.StreamHandler()
                ]
            )


def run(ogn_dir: str, rep_dir: str, period: int, log_file: str):
    observer = Observer()
    handler = EventHandler(log_file)
    observer.schedule(handler, ogn_dir, recursive=True)
    observer.start()
    try:
        while True:
            shutil.rmtree(rep_dir)
            os.mkdir(rep_dir)
            shutil.copytree(ogn_dir, rep_dir)
            time.sleep(period)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

