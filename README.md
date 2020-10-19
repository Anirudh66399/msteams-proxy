# msteams-proxy
Updated for latest ms teams app

A proxy program for ms teams which joins the classes on your behalf.

All the files mentioned above are important for the program the work.

It is a really simple program which gets the job done and can be edited to your preference or your classes timings,time table etc.

It doesn't give the roll calls on your behalf,it justs joins and leaves the classes on the time specified in the program.I know that is a big issue but i am working on it so till then you can ask your friends to call you if there is a rollcall else just sleep.

Remember to change the directory path to the ms teams application in your computer.

How to do it-

Simply just right click on the ms teams desktop icon ,click on properties and copy the target path and replace it with my path in os.system call in the launch function.
Remember to use " " for space,if there is any,in your username as i did else the program won't start.
EG- Anirudh" "Parihar

To change the time table according to your class timing,just edit the classes function and pass the new timings as args in enter() functions.

IMPORTANT
1. Remember to launch teams in 100% zoom else the program won't work.To edit the zoom settings just open the application and press ctrl and scroll with mouse wheel or press ctrl and use + or - keys.
2. Remember to download all the functions mentioned at the top of the .py file.
    To do so
    1. open the path where python is installed in your system
        For me it is "C:\Users\Anirudh Parihar\AppData\Local\Programs\Python\Python38"
    2. Open the scripts folder in it and copy the path
        C:\Users\Anirudh Parihar\AppData\Local\Programs\Python\Python38\Scripts
        
    3. open cmd and write cd *space* and paste the path and press enter
    
    4. Now,just google the modules mentioned at the top of the file and write their command
        example- pip install pyautogui

3. My python version at the time of writing this program is python3.8.5(64-bit),so download a version same or higher to this.Remember to donwload the 64-bit version only else the program won't be able to interact with ms-teams.

4. Make sure the python script and the files are all place in the same folder only else the program won't be able to access them.

5. This is a simple program which uses the given images in the folder and then searches them on the current screen using pyautogui module and when found, it clicks on them.So when using this program make sure nothing pops up on the screen in between else it won't be able to find the objects on the screen and hence give an error.

6. You can also use the sleep function to sleep the function till your 1st class like 10am in my case so ou won't have to wake up in the morning to run the program to.
    To do that simply type sleep(10,00)[in my case for 10am in the morning] just before calling launch() in the last 6th line  and run the program and your program will sleep till the time specified in the morning and then execute the rest of the code.
    
7. I hope i have made everything clear to you and if you still have doubts ,feel free to contact me 
    https://www.linkedin.com/in/anirudh-parihar-64b89b1a7/

Enjoy Free Proxiessssssssssss
