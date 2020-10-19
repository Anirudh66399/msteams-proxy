import os
import time
import pyautogui
import datetime
import pywinauto



#To Link Teams To pywinauto and restore meeting window
def call():
    
    dlg1=app.window(title_re=".*Call in progress*")
    dlg1.restore()





#Launch function to launch ms teams and click on calendar
def launch():
    
    os.system(r'start C:\Users\Anirudh" "Parihar\AppData\Local\Microsoft\Teams\Update.exe --processStart "Teams.exe"')
    time.sleep(10)
    



#functioon to sleep until specified time   
def sleep(y,z):
        x=datetime.datetime.now()
        target_time=datetime.datetime(x.year,x.month,x.day,y,z)
        
        while datetime.datetime.now() < target_time:
            
            time.sleep(10)


#Function to join class 
def enter(a,b):

    try:
        pyautogui.click('calendarloc.png')

    except:
        pyautogui.click('calendarloc2.png')
        
    time.sleep(5)

    
    pyautogui.move(400,0)
    pyautogui.scroll(-90)
    time.sleep(2)
    pyautogui.click()
    
    time.sleep(5)


    try:
        pyautogui.click('join.png')
    except:
        pyautogui.click('join1.png')
        
    time.sleep(5)




    try:
        pyautogui.click('audio.png')

    except:
        pass


    sleep(a,b)
    
    pyautogui.click(946,526)
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'shift', 'B')

        
    try:
        call()
        time.sleep(3)
        pyautogui.click(1738,915)
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'shift', 'B')
    
    except:
        pass
    
   
    time.sleep(5)

    
    try:
        dlg2=app.window(title_re=".*Microsoft Teams*")
        dlg2.restore()
    except:
        launch()



        
#To Attend Class
def classes():
    
    enter(11,2)                                        #mon10-11

     
    enter(12,2)                                        #11-12
  


    sleep(13,2)                                #12-1 break

    enter(15,2)                                 #1-3 lab
    
    enter(16,2)                                          #3-4 


    c=datetime.datetime.now()
    if c.strftime("%A")=="Thursday":                #Thursday class 4-5
        enter(17,2)



#End of functions


time.sleep(5)


launch()


#Linking process for link function
app=pywinauto.Application()
app.connect(title_re=".*Microsoft Teams*",best_match="Microsoft Teams")

   
time.sleep(5)


classes()

