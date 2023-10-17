import sys
import logging
import os
import yt_dlp
import time
from urllib.parse import urlparse, parse_qs
import json
# import unicodedata
from plyer import notification

filename = ''
filepath = ''
# Windows path
SAVE_PATH = os.path.expanduser("~\\Downloads\\")
print("SAVE_PATH: ", SAVE_PATH)

if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

# Get the path of the current Python script
script_path = os.path.abspath(sys.argv[0])
script_dir = os.path.dirname(script_path)

FORMAT = '[%(levelname)-5s][%(asctime)s] %(message)s'
logging.basicConfig(handlers=[logging.FileHandler(filename=os.path.join(
    script_dir, 'log_ytd_subprocess.log'), encoding='utf-8')], 
    format=FORMAT, level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

def my_hook(d):
    if d['status'] == 'finished':
        global filename, filepath
        # filename = d['info_dict']['title']
        filename = d['filename'].split('.')[0]
        filepath = d['info_dict']['filename']
        with open('log_d.log', 'w') as f:
            f.write(json.dumps(d, indent=4))


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
    try:
        # Read input from the main process
        input_data = sys.stdin.readline().split('\n')[0]
        logging.info("Input_data: " + input_data)
        # input_data = "https://www.youtube.com/watch?v=9n1aOSXX180&format=bestaudio"

        # Parse the URL
        parsed_url = urlparse(input_data)

        # Extract the query parameters as a dictionary using parse_qs
        query_parameters = parse_qs(parsed_url.query)
        # logging.info(query_parameters['v'])

        # Get the value of a specific parameter
        format_value = query_parameters['format'][0]
        # v_value = query_parameters.get('v', None)
        request_url = "https://www.youtube.com/watch?v=" + \
            query_parameters['v'][0]
        logging.info("request_url: " + request_url)

        # choose the file format you want, some versions of python3 cannot use match function
        if format_value == 'mp4':
            ydl_opts['format'] = 'bestvideo*[ext=mp4][height<=1080]+bestaudio[ext=m4a]/bestvideo+bestaudio'
        elif format_value == 'bestaudio':
            ydl_opts['format'] = 'bestaudio[ext=m4a]/bestaudio'

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([request_url])

        if os.path.exists(filepath):
            # Get the current time
            current_time = time.time()
            # Update the file's access and modification timestamps to the current time
            os.utime(filepath, (current_time, current_time))
            # Process the input and produce output

            output_data = "Success:" + filepath

            logging.info("Finished: " + request_url)
        else:
            # Process the input and produce output
            output_data = f"Failed: {input_data}"

        # Send the output to the main process
        logging.info('output_data: ' + output_data)
        sys.stdout.buffer.write(output_data.encode('utf-8'))
        sys.stdout.flush()

    except Exception as e:
        logging.exception(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
