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
            # message = nativemessaging.get_message()
            # logging.info("message: "+message)
            message = "https://www.youtube.com/watch?v=dZbU19tD0qA&format=bestaudio"
            if message.startswith("https://www.youtube.com/watch?v="):
                # nativemessaging.send_message(nativemessaging.encode_message("Processing..."))
                logging.info('TEST')
                # Launch the subprocess
                subprocess_args = ["python", "ytd_subprocess.py"]  # Command to run the subprocess
                subprocess_obj = subprocess.Popen(subprocess_args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                # Communicate with the subprocess
                input_data = message
                subprocess_obj.stdin.write(input_data)
                subprocess_obj.stdin.flush()

                output_data = subprocess_obj.stdout.read()
                error_data = subprocess_obj.stderr.read()

                # Wait for the subprocess to finish
                subprocess_obj.wait()
                if output_data.split('\n')[-1].split(':')[0] == 'Success':
                    logging.info('OK')
                else:
                    logging.info('SHIT')

                # # Print the output and error from the subprocess
                # print("Output from subprocess:")
                # print('output_data:', output_data.split('\n')[-1].split(':')[0])

                # print("Error from subprocess:")
                # print(error_data)
                break

        except Exception as e:
            logging.exception(e)
            break

if __name__ == "__main__":
    main()