# Lite Youtube Downloader - Chrome Extension
Based on the GitHub project yt-dlp  

## How to use

1. Load the unpacked Chrome extension on your Chrome browser  
   The path of the source code is under the directory src/  
   <img src="https://i.imgur.com/MQS1uJb.png" alt="chrome extension" width="500">  


3. Modify the host URL under the file src/download.js  
   For example:
   ```javascript
   host = 'http://the.host.url.you.want:5000/api/file'
   // Such as
   // host = 'http://localhost:5000/api/file'
   ``` 
   We are going the run the Python server on this device with port 5000  

4. Run the Python server on your host with the script:  
   Make sure your device has Python3 and pip3 installed  
   This script will start the server and make sure the other Python packages are installed:  
   ```bash
   # bash of your device
   sh run_wsgi_ws.sh
   ```
6. Open the page of the YouTube video you want to download,  
   Click the icon of the loaded Chrome extension to download the video or audio you want  

# Note

## Compile

To install a standalone pyinstaller for yt-dlp,  
You can follow the instructions of the origin project(yt-dlp)   
in order to compile your own project.  

See [description_about_yt-dlp](https://github.com/yt-dlp/yt-dlp#compile)  

```bash
pyinstaller.exe -F youtube-downloader-v2.py
```
