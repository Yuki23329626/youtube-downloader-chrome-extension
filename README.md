# Lite Youtube Downloader - Chrome Extension
Based on the GitHub project [yt-dlp](https://github.com/yt-dlp/yt-dlp)  
Note that this project is under development, so you may encounter several bugs.  
Feel free to report them.  

## How to use - Local version(Native Messaging)

1. Execute src/install.bat on Windows, and remember the path you install the native app

2. Load the unpacked Chrome extension(directory) on your Chrome browser  
   The path of the source code is the path you install the native app
   <img src="https://i.imgur.com/ruBCZAm.png" alt="chrome extension" width="800">  

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
