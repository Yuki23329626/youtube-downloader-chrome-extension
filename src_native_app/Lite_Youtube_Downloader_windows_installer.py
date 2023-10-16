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

# Tell system to aware the process DPI
ctypes.windll.shcore.SetProcessDpiAwareness(1)
# Get scale factor from device
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)

def browse_directory():
    global dir_installation
    dir_installation = filedialog.askdirectory(title="Select a Directory")
    dir_installation = os.path.normpath(dir_installation).replace("/", "\\")
    entry_path.delete(0, tk.END)
    entry_path.insert(0, dir_installation)

def confirm_removal(directory):
    # Create a confirmation pop-up dialog
    confirmation = messagebox.askyesno(
        "Confirmation", f"Directory already exist, overwrite '{directory}'?")
    return confirmation


def add_reg(dir_path):
    # Specify the registry key path and name
    key_path = r"SOFTWARE\Google\Chrome\NativeMessagingHosts\com.example.nativeapp"
    value_name = None

    # Specify the value data (e.g., a string)
    value_data = dir_path + "\\native_messaging_host.json"
    logging.info('value_data: ' + value_data)

    # Open the registry key for writing
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                             key_path, 0, winreg.KEY_WRITE)
        # Specify the name of the environment variable to append to
        var_name = "Path"
        # Specify the value you want to append
        new_value = os.path.join(dir_path, 'ffmpeg', 'bin')
        # Retrieve the current value of the environment variable
        current_value = os.environ.get(var_name, "")
        # Split the current value into a list of values using semicolon as the separator
        values_list = current_value.split(';')
        if new_value not in values_list:
            # Append the new value (separated by a semicolon) to the current value
            updated_value = f"{current_value};{new_value}"
            # Use the 'setx' command to update the environment variable
            try:
                subprocess.check_call(['setx', var_name, updated_value])
                logging.info(
                    f"Appended '{new_value}' to environment variable {var_name}")
            except Exception as e:
                logging.exception(e)

    except PermissionError as e:
        logging.error(e)
        # Create a message box with text and an OK button
        message = "Access is denied. In order to register the native application on Windows Registry, please run this executable as admin"
        title = "Access Required"
        messagebox.showinfo(title, message)
        sys.exit(1)
    except FileNotFoundError as e:
        # If the key doesn't exist, create it
        logging.info('key doesn\'t exist, create it')
        key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path)

    # # Open the registry key for writing
    # try:
    #     key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
    # except FileNotFoundError as e:
    #     # If the key doesn't exist, create it
    #     logging.info('key doesn\'t exist, create it')
    #     key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)

    try:
        path_json_file = 'native_messaging_host.json'

        data = {
            "name": "com.example.nativeapp",
            "description": "Example Native Messaging Host",
            "path-origin": "D:\\git\\youtube-downloader-chrome-extension\\src_native_app\\native_host.py",
            "path": "C:\\Users\\micha\\src_native_app\\native_host.py",
            "type": "stdio",
            "allowed_origins": [
                "chrome-extension://oaabembeldgibjbdkgdnpekfoodledoh/",
                "chrome-extension://odpjnifkinoeflcohfepblkdhnjglkpj/",
                "chrome-extension://kbhloehkeldjmihnhinchnkkiajbimek/"
            ]
        }

        with open(path_json_file, "w") as json_file:
            if getattr(sys, 'frozen', False):
                # The script is running as an executable (e.g., using PyInstaller or cx_Freeze)
                print("Running as an executable")
                executable_path = sys.executable
                print("Executable path:", executable_path)
                data['path'] = dir_path + "\\native_host.exe"
            else:
                # The script is running as a regular Python script
                print("Running as a Python script")
                script_name = sys.argv[0]
                print("Script name:", script_name)
                data['path'] = dir_path + "\\native_host.py"
            json.dump(data, json_file, indent=4)
            # os.system('pause')
    except Exception as e:
        logging.exception(e)

    # Set the registry value
    winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, value_data)

    # Close the registry key
    winreg.CloseKey(key)

    logging.info(
        f"Registry key '{key_path}\\{value_name}' added with value '{value_data}'.")


def submit():
    try:
        global dir_installation
        logging.info('Submit, dir_installation:' + dir_installation)
        # Get the name of the source directory
        source_directory_name = os.path.basename(script_dir)
        print('source_directory_name: ', source_directory_name)
        DEFAULT_DIRNAME = 'LiteYTD'
        dir_shutil = os.path.join(dir_installation, DEFAULT_DIRNAME)
        # Delete the destination directory if it exists
        if os.path.exists(dir_shutil):
            if not confirm_removal(dir_shutil):
                sys.exit(0)
        # print(dir_shutil)
        add_reg(dir_shutil)
        if script_dir == dir_shutil:
            sys.exit(0)
        shutil.copytree(script_dir, dir_shutil, dirs_exist_ok=True)
        sys.exit(0)
    except Exception as e:
        logging.exception(e)


try:
    # Create the main tkinter window
    root = tk.Tk()
    root.tk.call('tk', 'scaling', ScaleFactor/75)
    root.title("Lite Youtube Downloader - Setup")
    root.iconbitmap(os.path.join(script_dir, 'installer.ico'))  # Replace "custom_icon.ico" with the path to your icon file

    # Create a frame to hold the label and entry
    frame = tk.Frame(root)
    frame.pack(pady=10)

    # Create a label
    label = tk.Label(frame, text="Custom install location:")
    label.grid(row=0, sticky='w', padx=10)

    # Create an entry field for path input with default text
    DEFAULT_PATH = os.path.normpath(os.path.expanduser("~")).replace("/", "\\")
    dir_installation = DEFAULT_PATH
    entry_path = tk.Entry(frame, width=40)
    entry_path.insert(0, DEFAULT_PATH)
    entry_path.grid(row=1, column=0, padx=12)

    # Create a "Browse" button
    browse_button = tk.Button(frame, text="Browse",
                              command=browse_directory, width=10)
    browse_button.grid(row=1, column=1, padx=12, pady=12)

    # Create a "Browse" button
    browse_button = tk.Button(frame, text="Install", command=submit, width=10)
    browse_button.grid(row=2, column=1, padx=12, sticky='e')

    # Start the tkinter event loop
    root.mainloop()
except Exception as e:
    logging.exception(e)
