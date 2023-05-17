import yt_dlp

SAVE_PATH = 'cache/'

str_link = 'https://www.youtube.com/watch?v=pvGTPEcqGZY'
link = [str_link]

def my_hook(d):
    if d['status'] == 'finished':
        global filename
        # filename = d['info_dict']['title']
        filename = d['filename'].split('.')[0]

ydl_opts = {
    'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    # 'format': 'bestvideo/best',
    # 'format': 'bestaudio/best',
    # 'postprocessors': [{
    #     'key': 'FFmpegExtractAudio',
    #     'preferredcodec': 'mp3',
    #     'preferredquality': '192',
    # }],
    # 'skip_download': True,
    # 'writesubtitles': False,
    'progress_hooks': [my_hook],
    'outtmpl': SAVE_PATH + '%(title)s.%(ext)s'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(link)
