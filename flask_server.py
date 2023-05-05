from flask import Flask, jsonify, send_file, request
import yt_dlp
import logging
import os

filename = ''
SAVE_PATH = os.getcwd() + '/cache'
# print(SAVE_PATH)

def my_hook(d):
    if d['status'] == 'finished':
        global filename
        filename = d['filename']

ydl_opts = {
    'skip_download': False,
    'writesubtitles': True,
    'progress_hooks': [my_hook],
    'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s'
}

app = Flask(__name__)

@app.route('/api/file')
def get_file():

    try:
        link = request.args.get('url')
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(link)
        return send_file(filename, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)})

# @app.after_request
# def after_request_func(response):
#     # Do something after the request has been processed
#     filename=''
#     os.remove(filename)
#     return response

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
