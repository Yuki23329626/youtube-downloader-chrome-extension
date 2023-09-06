
import logging
import os
import logging
import nativemessaging
from urllib.parse import urlparse, parse_qs
import subprocess
from time import sleep
from plyer import notification

# Get the path of the current Python script
script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)

FORMAT = '[%(levelname)s][%(asctime)s] %(message)s'
logging.basicConfig(handlers=[logging.FileHandler(filename='log.native_host', encoding='utf-8')], format=FORMAT, level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

def main():
    while True:
        try:
            message = nativemessaging.get_message()
            # logging.info("message: "+message)
            # message = "https://www.youtube.com/watch?v=9n1aOSXX180&format=bestaudio"
            if message.startswith("https://www.youtube.com/watch?v="):
                nativemessaging.send_message(nativemessaging.encode_message("Processing, please wait..."))
                logging.info('Processing: ' + message)
                # Launch the subprocess
                subprocess_args = ["python", "ytd_subprocess.py"]  # Command to run the subprocess
                # subprocess_args = ["ytd_subprocess.exe"]  # Command to run the subprocess
                subprocess_obj = subprocess.Popen(subprocess_args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=False)

                # Communicate with the subprocess
                stdout_byte, stderr_byte = subprocess_obj.communicate(input=message.encode('utf-8'))
                output_data = stdout_byte.decode('utf-8')

                # It is only recommended to cancel the following comment when debugging
                logging.info(' ===== output_data: ===== \n' + output_data)

                result = output_data.split('\n')[-1].split(':')
                if result[0] == 'Success':
                    nativemessaging.send_message(nativemessaging.encode_message("Finished"))
                    logging.info('Success: ' + message)

                     # Title and message for the notification
                    title = "Download finished"
                    message = ':'.join(result[1:])

                    # Create and display the notification
                    notification.notify(
                        title=title,
                        message=message,
                        app_name="Lite Youtube Downloader",  # Specify your application's name
                        timeout=10,              # The notification will automatically close after 10 seconds (optional)
                    )
                    
                else:
                    nativemessaging.send_message(nativemessaging.encode_message("403 Forbidden: Cannot download"))
                    logging.info('Failed: ' + message)

                # # Print the output and error from the subprocess
                # print("Output from subprocess:")
                # print('output_data:', output_data.split('\n')[-1].split(':')[0])

                # print("Error from subprocess:")
                # print(error_data)
                break
            else:
                nativemessaging.send_message(nativemessaging.encode_message("Invalid URL"))
                continue

        except Exception as e:
            logging.exception(e)
            break

if __name__ == "__main__":
    main()