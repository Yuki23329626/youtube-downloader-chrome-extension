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

filename = ''
# Windows path
SAVE_PATH = os.path.expanduser("~\\Downloads\\")
# print("SAVE_PATH: ", SAVE_PATH)

if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

# Get the path of the current Python script
script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)

FORMAT = '[%(levelname)s][%(asctime)s] %(message)s'
logging.basicConfig(handlers=[logging.FileHandler(filename='log.native_host', encoding='utf-8')], format=FORMAT, level=logging.INFO, datefmt = '%Y-%m-%d %H:%M:%S')

def main():
    # ydl_opts['format'] = 'bestaudio'
    # with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    #     ydl.download(["https://www.youtube.com/watch?v=dZbU19tD0qA"])
    while True:
        try:
            message = nativemessaging.get_message()
            # logging.info("message: "+message)
            # message = "https://www.youtube.com/watch?v=9n1aOSXX180&format=bestaudio"
            if message.startswith("https://www.youtube.com/watch?v="):
                nativemessaging.send_message(nativemessaging.encode_message("Processing, please wait..."))
                logging.info('Processing: ' + message)
                # Launch the subprocess
                subprocess_args = ["python", "ytd_subprocess.py"]  # Command to run the subprocess
                subprocess_obj = subprocess.Popen(subprocess_args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                # Communicate with the subprocess
                input_data = message + '\n'
                subprocess_obj.stdin.write(input_data)
                subprocess_obj.stdin.flush()

                output_data = subprocess_obj.stdout.read()
                # error_data = subprocess_obj.stderr.read()

                # Wait for the subprocess to finish
                subprocess_obj.wait()
                # logging.info(output_data)
                if output_data.split('\n')[-1].split(':')[0] == 'Success':
                    nativemessaging.send_message(nativemessaging.encode_message("Finished"))
                    logging.info('Success: ' + message)
                else:
                    nativemessaging.send_message(nativemessaging.encode_message("403 Forbidden: Cannot download"))
                    logging.info('Failed: ' + message)

                # # Print the output and error from the subprocess
                # print("Output from subprocess:")
                # print('output_data:', output_data.split('\n')[-1].split(':')[0])

                # print("Error from subprocess:")
                # print(error_data)
                # break
            else:
                nativemessaging.send_message(nativemessaging.encode_message("Invalid URL"))
                continue

        except Exception as e:
            logging.exception(e)
            break

if __name__ == "__main__":
    main()