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
import subprocess

FORMAT = '[%(levelname)s][%(asctime)s] %(message)s'
logging.basicConfig(handlers=[logging.FileHandler(filename='log.native_host', encoding='utf-8')], format=FORMAT, level=logging.INFO)
logging.info("Start")

filename = ''
# Windows path
SAVE_PATH = os.path.expanduser("~\\Downloads\\")
print("SAVE_PATH: ", SAVE_PATH)

if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

# Get the path of the current Python script
script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)

def my_hook(d):
    if d['status'] == 'finished':
        global filename
        # filename = d['info_dict']['title']
        filename = d['filename'].split('.')[0]
        print("\nfilename1:" + filename)
        # with open("log.filename", 'w') as file:
        #     file.write(json.dumps(d, indent=4))
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
    # ydl_opts['format'] = 'bestaudio'
    # with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    #     ydl.download(["https://www.youtube.com/watch?v=dZbU19tD0qA"])
    while True:
        try:
            message = nativemessaging.get_message()
            # logging.info("message: "+message)
            # message = "https://www.youtube.com/watch?v=dZbU19tD0qA&format=bestaudio"
            if message.startswith("https://www.youtube.com/watch?v="):
                nativemessaging.send_message(nativemessaging.encode_message("Processing..."))

                # Parse the URL
                parsed_url = urlparse(message)

                # Extract the query parameters as a dictionary using parse_qs
                query_parameters = parse_qs(parsed_url.query)
                # logging.info(query_parameters['v'])

                # Get the value of a specific parameter
                format_value = query_parameters['format'][0]
                # v_value = query_parameters.get('v', None)
                request_url = "https://www.youtube.com/watch?v=" + query_parameters['v'][0]
                logging.info("request_url: " + request_url)

                # choose the file format you want, some versions of python3 cannot use match function
                if format_value == 'mp4':
                    ydl_opts['format'] = 'bestvideo*[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio'
                elif format_value == 'bestaudio':
                    ydl_opts['format'] = 'bestaudio[ext=m4a]/bestaudio'

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([request_url])
                    break
        except Exception as e:
            logging.exception(e)
            # break

if __name__ == "__main__":
    main()