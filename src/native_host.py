import sys
import json
import logging
import os
import struct
import yt_dlp
import logging
import time
from pathlib import Path
import nativemessaging


filename = ''
SAVE_PATH = os.path.expanduser("~\Downloads") 
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)
# print('SAVE_PATH', SAVE_PATH)

# Get the path of the current Python script
script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)

FORMAT = '[%(levelname)s][%(asctime)s] %(message)s'
logging.basicConfig(handlers=[logging.FileHandler(filename='log.native_host', encoding='utf-8')], format=FORMAT, level=logging.INFO)
logging.info("Start")

def my_hook(d):
    if d['status'] == 'finished':
        global filename
        # filename = d['info_dict']['title']
        filename = d['filename'].split('.')[0]
        logging.info("\nfilename1:", filename)

# options for the yt-dlp(github project)
ydl_opts = {
    # 'format': 'bestaudio/best',
    # 'postprocessors': [{
    #     'key': 'FFmpegExtractAudio',
    #     'preferredcodec': 'mp3',
    #     'preferredquality': '192',
    # }],
    # 'skip_download': False,
    'writesubtitles': False,
    'progress_hooks': [my_hook],
    'outtmpl': SAVE_PATH + '%(title)s.%(ext)s',
    'nooverwrites': False
}

def main():
    while True:
        try:
            message = nativemessaging.get_message()
            if message == "hello":
                nativemessaging.send_message(nativemessaging.encode_message("world"))
        except Exception as e:
            logging.exception(e)
            break

if __name__ == "__main__":
    main()