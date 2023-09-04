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

def process_message(message):
    # Process the message and prepare a response.
    response = {'message': f'Received message from extension: {message["text"]}'}
    return response

def main():
    # # 1.windows：\r\n -> \n
    # if sys.platform == "win32":
    #     import msvcrt
    #     msvcrt.setmode(sys.stdin.fileno(), os.O_BINARY)
    #     msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)

    while True:
        try:
            ctl = CrxToLocal()
            ctl.read_message()
            logging.info("Receiving message...")
            ctl.handle_message()
            logging.info("Processing...")
            ctl.send_message()
            logging.info("Returning result...")
        except Exception as e:
            logging.exception(e)


class CrxToLocal:
    def __init__(self):
        self._input_body = None
        self._output_body = None

    def read_message(self):
        # reading stdin msg-header(first 4 bytes).
        text_length_bytes = sys.stdin.buffer.read(4)

        # Unpack message length as 4 byte integer, tuple = struct.unpack(fmt, buffer).
        text_length = struct.unpack("I", text_length_bytes)[0]

        # reading stdin msg-body bytes
        self._input_body = sys.stdin.buffer.read(text_length)

    def handle_message(self):
        # with open("./local_file.json", "a", encoding="utf-8") as f:
        #     json.dump(json.loads(self._input_body, encoding="utf-8"), f, ensure_ascii=False, indent=2)
        json_message = json.loads(self._input_body)
        logging.info("message: " + json.dumps(json_message))

        # _output_body need to be JSON utf-8 bytes
        self._output_body = json.dumps({"response": "Nice to meet you."}).encode("utf-8")

    def send_message(self):
        # write msg-header to stdout, I means int type which contians 4 bytes，reference: python-doc/library/struct
        sys.stdout.buffer.write(struct.pack("I", len(self._output_body)))
        # write msg-body to stdout
        sys.stdout.buffer.write(self._output_body)
        sys.stdout.flush()


if __name__ == "__main__":
    main()