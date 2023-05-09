from flask import Flask, jsonify, send_file, request, after_this_request
import yt_dlp
import logging
import glob, os
import time
from threading import Thread

filename = ''
SAVE_PATH = 'cache/'
# print('SAVE_PATH', SAVE_PATH)

logging.basicConfig(level=logging.ERROR,
                    format='%(levelname)-8s %(asctime)s %(message)s',
                    datefmt='%yyyy-%m-%d %H:%M:%S',
                    handlers = [logging.FileHandler(SAVE_PATH + 'ytdlp_lite.log', 'w', 'utf-8'),])

def my_hook(d):
    if d['status'] == 'finished':
        global filename
        # filename = d['info_dict']['title']
        filename = d['filename'].split('.')[0]

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
    'outtmpl': SAVE_PATH + '%(title)s.%(ext)s'
}

app = Flask(__name__)

def remove_file(file):
    time.sleep(2)
    try:
        os.remove(file)
    except Exception as e:
        print(e)

@app.route('/api/file')
def get_file():
    try:
        parameters = request.args.to_dict()
        link = parameters.pop('url')
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(link)
        list_files = glob.glob(filename + '*')
        # print('filename: ', filename)
        @after_this_request
        def after_request(response):
            t = Thread(target=remove_file, args=(list_files[0],))
            t.start()
            return response
        return send_file(list_files[0], as_attachment=True)
    except Exception as e:
        logging.error(e)
        template = "An exception of type {0} occurred."
        message = template.format(type(e).__name__)
        return message

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