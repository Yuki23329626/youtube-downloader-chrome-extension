from flask import Flask, jsonify, send_file, request, after_this_request, make_response
# import asyncio
import yt_dlp
import logging
import glob
import os
import time
import random
from threading import Thread
import sys
from pathlib import Path
import shutil
from flask_cors import CORS

filename = ''
BASE_PATH = 'cache/' # may replace by random number in future
target_path = ''
if not os.path.exists(BASE_PATH):
    os.makedirs(BASE_PATH)
# print('SAVE_PATH', SAVE_PATH)

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)-8s %(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.FileHandler('log_ytdlp_lite.log', 'w', 'utf-8'),])

# get the final filename after downloading the file

def my_hook(d):
    if d['status'] == 'finished':
        global filename
        # filename = d['info_dict']['title']
        filename = d['filename'].split('.')[0]
        print("\nfilename1:", filename)

app = Flask(__name__)
CORS(app)

# Remove downloaded file after serve the target file to the client

def remove_file(list_files):
    # time.sleep(20)
    directory_path = BASE_PATH + target_path
    try:
        logging.info('removing files: ' + directory_path)
        if os.path.exists(directory_path) and os.path.isdir(directory_path):
            shutil.rmtree(directory_path)
    except Exception as e:
        logging.error(e)

@app.route('/api/file')
async def get_file():
    # Get the current time as an integer
    current_time = int(time.time())
    # Use the current time as a seed for the random number generator
    random.seed(current_time)
    # Generate a random value, e.g., between 0 and 1
    random_value = hash(random.random())
    global target_path 
    target_path = str(random_value) + '/'
    SAVE_PATH = BASE_PATH + target_path
    if not os.path.exists(SAVE_PATH):
        os.makedirs(SAVE_PATH)

    print('request', request)
    v = request.args.get('v')
    file_format = request.args.get('format')
    print('v', v)
    print('file_format', file_format)
    url = ''
    try:
        url = 'https://www.youtube.com/watch?v=' + v
    except Exception as e:
        logging.error(e)

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

    # choose the file format you want, some versions of python3 cannot use match function
    if file_format == 'bestaudio':
        ydl_opts['format'] = 'bestaudio[ext=m4a]/bestaudio'
        # ydl_opts['postprocessors'] = [{
        #     'key': 'FFmpegExtractAudio',
        #     'preferredcodec': 'mp3',
        #     'preferredquality': '192'
    elif file_format == 'mp4':
        print('file_format', file_format)
        # ydl_opts['format'] = 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        ydl_opts['format'] = 'bestvideo*[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio'

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)
    # print('filename2:', filename)
    # list_files = glob.glob(filename + '*')

    
    relative_path = SAVE_PATH
    prefix = filename.split('/')[-1].split('\\')[-1]
    print("prefix:", prefix)

    absolute_path = os.path.abspath(relative_path)
    list_files = [file for file in os.listdir(absolute_path) if file.startswith(prefix)]

    logging.info('list_files: ' + str(list_files))
    
    @after_this_request
    def after_request(response):
        t = Thread(target=remove_file, args=(list_files,))
        t.start()
        return response
    
    # Create a Path object
    path_obj = Path(list_files[0])

    # Extract the file name using Path.name
    filename_ = path_obj.name

    # if True:
    #     error_message = "An error occurred."
    #     return jsonify({'error': error_message}), 400
    
    return send_file(SAVE_PATH+list_files[0], as_attachment=True, download_name=filename_)

    # # Create a response object
    # response = make_response(send_file(list_files[0], as_attachment=True, download_name=filename_))

    # # Add custom attributes to the response headers
    # print('filename_:', filename_)
    # response.headers['Content-Disposition'] = f'attachment; filename="{filename_}"'

    # if file_format == 'bestaudio':
    #     response.headers['Content-Type'] = f'audio/mpeg'
        
    # return response
        

    # except Exception as e:
    #     logging.error(e)
    #     template = "An exception of type {0} occurred."
    #     message = template.format(type(e).__name__)
    #     return message

# @app.route('/api/file')
# def get_file():
#     parameters = request.args.to_dict()
#     link = parameters.pop('url')
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download(link)
#     list_files = glob.glob(filename + '*')
#     response = send_file(SAVE_PATH + '\\' + list_files[0])
#     @after_this_request
#     def remove_file(response):
#         print('File download complete')
#         os.remove(SAVE_PATH + '\\' + list_files[0])
#         return response
#     return response

# @app.after_request
# def after_request_func(response):
#     # Do something after the request has been processed
#     list_files = glob.glob(filename + '*')
#     while True:
#         time.sleep(5)
#         try:
#             os.remove(list_files[0])
#             break
#         except:
#             pass
#     return response


if __name__ == '__main__':
    # app.run(debug=True, host="0.0.0.0",ssl_context=('/etc/letsencrypt/archive/nxshen.csie.io-0002/cert1.pem', '/etc/letsencrypt/archive/nxshen.csie.io-0002/privkey1.pem'))
    app.run(debug=True, host="0.0.0.0")