import yt_dlp

link = ['https://www.youtube.com/watch?v=1P5GjS48UeM']

ydl_opts = {'skip_download': False, 'writesubtitles': True}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(link)