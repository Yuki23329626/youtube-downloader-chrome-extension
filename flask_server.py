from flask import Flask, jsonify, send_file, request, after_this_request, make_response
import asyncio
import yt_dlp
import logging
import glob
import os
import time
from threading import Thread
import re
from pathlib import Path

filename = ''
SAVE_PATH = 'cache/'
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)
# print('SAVE_PATH', SAVE_PATH)

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)-8s %(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.FileHandler(SAVE_PATH + 'ytdlp_lite.log', 'w', 'utf-8'),])

# get the final filename after downloading the file


def my_hook(d):
    if d['status'] == 'finished':
        global filename
        # filename = d['info_dict']['title']
        filename = d['filename'].split('.')[0]
        print("\nfilename1:", filename)


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

app = Flask(__name__)

# Remove downloaded file after serve the target file to the client

def remove_file(file):
    time.sleep(20)
    while glob.glob(file):
        try:
            print('removing files:', file)
            os.remove(glob.glob(file)[0])
        except Exception as e:
            print(e)

@app.route('/api/file')
async def get_file():
    # try:
    # pop the parameters from the url
    parameters = request.args.to_dict()
    # link = parameters.pop('url')
    request_string = request.url
    print('request_string', request_string)
    logging.info('\n[Success]: ' + request_string)
    url = parameters.get('url')
    print('url', url)
    file_format = parameters.get('format')

    # choose the file format you want, some versions of python3 cannot use match function
    if file_format == 'mp4':
        print('file_format', file_format)
        # ydl_opts['format'] = 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        ydl_opts['format'] = 'bestvideo*[ext=mp4]+bestaudio[ext=m4a]'
    elif file_format == 'bestaudio':
        ydl_opts['format'] = 'bestaudio[ext=m4a]/bestaudio'
        # ydl_opts['postprocessors'] = [{
        #     'key': 'FFmpegExtractAudio',
        #     'preferredcodec': 'mp3',
        #     'preferredquality': '192'
        # }]

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)
    print('filename2:', filename)
    list_files = glob.glob(filename + '*')
    print('list_files:', list_files)
    
    @after_this_request
    def after_request(response):
        t = Thread(target=remove_file, args=(list_files[0],))
        t.start()
        return response
    
    # Create a Path object
    path_obj = Path(list_files[0])

    # Extract the file name using Path.name
    filename_ = path_obj.name
    
    return send_file(list_files[0], as_attachment=True, download_name=filename_)

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
    app.run(debug=True, host="0.0.0.0")
