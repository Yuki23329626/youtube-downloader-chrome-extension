import tkinter as tk
from tkinter import filedialog
import os
import shutil
import logging
from tkinter import messagebox
import ctypes
import winreg
import json
import sys
import subprocess

# Get the path of the current Python script
script_path = os.path.abspath(sys.argv[0])
script_dir = os.path.dirname(script_path)
print('script_dir: ', script_dir)

FORMAT = '[%(levelname)-5s][%(asctime)s] %(message)s'
logging.basicConfig(handlers=[logging.FileHandler(
    filename=os.path.join(script_dir, 'log_installer.log'), encoding='utf-8')],
    format=FORMAT, level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

REG_KEY_PATH = r"SOFTWARE\Google\Chrome\NativeMessagingHosts\com.example.nativeapp"
DEFAULT_HOME = os.path.normpath(os.path.expanduser("~")).replace("/", "\\")
DEFAULT_DIRNAME = 'LiteYTD'
dir_installation = DEFAULT_HOME

def handleException(e):
    logging.exception(e)
    # Create a message box with text and an OK button
    title = "Error"
    messagebox.showinfo(title, e)
    sys.exit(1)

def add_reg(dir_path):
    print("dir_path: " + dir_path + "\n")
    # # Specify the registry key path and name
    # value_name = None

    # # Specify the value data (e.g., a string)
    # value_data = dir_path + "\\native_messaging_host.json"
    # logging.info('value_data: ' + value_data)

    # # Open the registry key for writing
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                             REG_KEY_PATH, 0, winreg.KEY_WRITE)
        # Specify the name of the environment variable to append to
        var_name = "Path"
        # Specify the value you want to append
        new_value = os.path.join(dir_path, 'ffmpeg', 'bin')
        print("new_value:" + new_value + "\n")
        # Retrieve the current value of the environment variable
        current_value = os.environ.get(var_name, "")
        print("current_value:" + current_value + "\n")
        # Split the current value into a list of values using semicolon as the separator
        values_list = current_value.split(';')
        if new_value not in values_list:
            print("New value is not in value list\n")
            # Append the new value (separated by a semicolon) to the current value
            updated_value = f"{current_value};{new_value}"
            print("updated_value:",updated_value)
            # Use the 'setx' command to update the environment variable
            try:
                subprocess.check_call(['setx', var_name, updated_value])
                print("append\n")
            except Exception as e:
                handleException(e)

    except PermissionError as e:
        logging.exception(e)
        # Create a message box with text and an OK button
        message = "Access is denied. In order to register the native application on Windows Registry, please run this script as admin."
        title = "Access Required"
        messagebox.showinfo(title, message)
        sys.exit(1)
    except FileNotFoundError as e:
        # If the key doesn't exist, create it
        logging.info('key doesn\'t exist, create it')
        key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, REG_KEY_PATH)

add_reg(r"C:\Users\user\LiteYTD")