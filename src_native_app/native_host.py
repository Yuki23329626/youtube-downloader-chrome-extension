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
from urllib.parse import urlparse, parse_qs


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
        nativemessaging.send_message(nativemessaging.encode_message("Successfully Downloaded"))


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
            if message.startswith("https://www.youtube.com/watch?v="):
                nativemessaging.send_message(nativemessaging.encode_message("Processing: " + message))

                # Parse the URL
                parsed_url = urlparse(message)

                # Extract the query parameters as a dictionary using parse_qs
                query_parameters = parse_qs(parsed_url.query)

                # Get the value of a specific parameter
                format_value = query_parameters.get('format', None)
                url_value = query_parameters.get('url', None)
                logging.info(url_value)

                if format_value == 'mp4':
                    ydl_opts['format'] = 'bestvideo*[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio'
                elif format_value == 'bestaudio':
                    ydl_opts['format'] = 'bestaudio[ext=m4a]/bestaudio'

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download(url_value)
                
        except Exception as e:
            nativemessaging.send_message(" ===== Error Message =====\n" + e)
            logging.exception(e)
            break

if __name__ == "__main__":
    main()