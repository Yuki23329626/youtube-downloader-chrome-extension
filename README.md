# Lite Youtube Downloader - Chrome Extension
Based on the GitHub project [yt-dlp](https://github.com/yt-dlp/yt-dlp)  
Note that this project is under development, so you may encounter several bugs.  
Feel free to report them.  

## How to use - Local(Windows 10 executable)

1. Download application: [LiteYoutubeDownloader](https://mega.nz/file/yg5kkAja#BMsKvFb4oLLZuTO14jd6UtKe8cKoCdIjOxfOnmJov3o)

2. Execute LiteYoutubeDownloader/install.bat on Windows,  
   and remember the path of the directory you install the native app

3. Enable the Developer mode on your Chrome
   <img src="https://i.imgur.com/mxTnE6i.png" alt="Developer mode" width = "800">

4. Load the unpacked Chrome extension(directory) on your Chrome browser  
   The path of the source code is the path you install the native app
   <img src="https://i.imgur.com/7kazuX4.png" alt="chrome extension" width="600">  

## How to use - Local(Need Compile)

1. Install the necessary Python and packages
```cmd
PS D:\git> python --version
Python 3.11.5
PS D:\git> pip --version
pip 23.2.1 from C:\Users\micha\AppData\Local\Programs\Python\Python311\Lib\site-packages\pip (python 3.11)
```
```bash
pip install nativemessaging
pip install plyer
pip install yt_dlp
```

2. Install ffmpeg and add the Path of the ffmpeg on your system

3. Run Lite_Youtube_Downloader_windows_installer.py on Windows, and remember the directory path you install the native app

   ```cmd
   python Lite_Youtube_Downloader_windows_installer.py
   ```

4. Enable the Developer mode on your Chrome
   <img src="https://i.imgur.com/mn5mJ8y.png" alt="Developer mode" width = "800">

5. Load the unpacked Chrome extension(directory) on your Chrome browser  
   The path of the source code is the path you install the native app
   <img src="https://i.imgur.com/7kazuX4.png" alt="chrome extension" width="600">  

## How to use - Client-Server version

1. Load the unpacked Chrome extension(directory) on your Chrome browser  
   The path of the source code is under the directory src/  


3. Modify the host URL under the file src/download.js  
   For example:
   ```javascript
   host = 'http://the.host.url.you.want:5000/api/file'
   // Such as
   // host = 'http://localhost:5000/api/file'
   // host = 'http://127.0.0.1:5000/api/file'
   ``` 
   We are going the run the Python server on this device with port 5000  

4. Run a Python server on your host with the script:  
   Make sure your device has Python3 and pip3 installed
   ```bash
   admin@host:~$ python3 --version
   Python 3.8.10
   admin@host:~$ pip3 --version
   pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
   ```
   This script will start the server and make sure the other Python packages are installed:  
   ```bash
   sh run_wsgi_ws.sh
   ```
   If you want to stop the server, run the following bash script:
   ```bash
   sh kill_gunicorn.sh
   ```
6. Open the page of the YouTube video you want to download,  
   Click the icon of the loaded Chrome extension to download the video or audio you want  

# Note

## Compile

To obtain a standalone pyinstaller for a project which contains yt-dlp,  
You can follow the instructions of the origin GitHub project(yt-dlp)   
to compile your own project.  

> PyInstaller is a popular Python packaging tool  
> that allows you to convert Python applications into standalone executables (or standalone apps) 

See [description_about_yt-dlp](https://github.com/yt-dlp/yt-dlp#compile)  

```bash
pyinstaller.exe -F youtube-downloader-v2.py
```
