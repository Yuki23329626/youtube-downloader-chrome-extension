@echo off
:: Run Python script with admin rights
powershell -Command "Start-Process 'python.exe' -ArgumentList 'Lite_Youtube_Downloader_windows_installer.py' -Verb RunAs"