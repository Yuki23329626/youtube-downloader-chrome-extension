import yt_dlp
import logging
import json

def my_hook(d):
    if d['status'] == 'finished':
        print(d['filename'])


ydl_opts = {
    'skip_download': False,
    'writesubtitles': True,
    'progress_hooks': [my_hook]
}

while True:
    str_link = input('URL:')
    link = [str_link]
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(link)
    except Exception as e:
        logging.error(e)
