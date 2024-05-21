import speech_recognition as sr
import pyaudio
import pyttsx3
import os
import subprocess
import json
from tkinter import filedialog
import writeToJson as WJ
import pyttsx3 

r = sr.Recognizer()
shortcutsOpened = [None, None, None, None, None]
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(sentence):
    print(sentence)
    engine.say(sentence)
    engine.runAndWait() 


def add_command():
    #open file explorer
    talk("Select the file you would like the command to access.")
    newCommandPath1 = filedialog.askopenfilename()

    #returns to main loop if no file is selected
    if(newCommandPath1 == ""):
        talk("No New Command Added!")
        return""

    #ask if another file should be selected
    talk("Another path may be selected but is not requireed")
    newCommandPath2 = filedialog.askopenfilename()

    accepted = False

    #ask user to speak the name of application/set command name/get user to confirm command
    while(accepted == False):
        talk ("Please say the name of the command. This phrase will be precded by \'open\'")
        command = record_text()
        talk("Are you sure you want the command to be \'open "+ command +"\'")
        confirmation = ""
        while(confirmation != "no" and confirmation != "yes"):
            talk("Please respond with \'yes\' or \'no\'")
            confirmation = record_text()
            if(confirmation == "yes"):
                accepted = True

    #store the command
    talk("Which command would you like to overwrite")
    validResponse = False
    while(validResponse != True):
        talk("Please respond with \'number one\', \'number two\', etc")
        response = record_text()

        with open('paths.json') as file:
            paths = json.load(file)

        if(response == "number one"):
            validResponse = True
            WJ.write(0, newCommandPath1, newCommandPath2, command)

        elif(response == "number two"):
            validResponse = True
            WJ.write(1, newCommandPath1, newCommandPath2, command)
            
        elif(response == "number three"):
            validResponse = True
            WJ.write(2, newCommandPath1, newCommandPath2, command)
            
        elif(response == "number four"):
            validResponse = True
            WJ.write(3, newCommandPath1, newCommandPath2, command)
            
        elif(response == "number five"):
            validResponse = True
            WJ.write(4, newCommandPath1, newCommandPath2, command)


def open_file_from_shortcut(userInput, index):
    global shortcutsOpened

    #read paths from the json file
    with open('paths.json') as file:
        paths = json.load(file)

    #check if the command is correct
    if(userInput == "open "+ paths[index]["command"]):
        #check if file is already open
        if(shortcutsOpened[index] is None):
            talk("Opening "+ paths[index]["command"] +"...")
            #save path
            shortcutsOpened[index] = subprocess.Popen([paths[index]["primary_path"], paths[index]["secondary_path"]])
            #shortcutsOpened[index] = subprocess.Popen(paths["primary_path"])
        else:
            talk(paths[index]["command"] +" is Already Open...")

def close_file_from_shortcut(userInput, index):
    global shortcutsOpened

    #read paths from the json file
    with open('paths.json') as file:
        paths = json.load(file)

    if(userInput == "close "+ paths[index]["command"]):
            if shortcutsOpened[index] is not None:
                talk("Closing "+ paths[index]["command"] +"...")
                shortcutsOpened[index].terminate()
                shortcutsOpened[index] = None
            else:
                talk(paths[index]["command"] +" Was Not Open...")

def record_text():
    r = sr.Recognizer()
    while(1):
        try:
            #tell jasmine to use the microphone
            with sr.Microphone() as source:
                try:
                #adjust audio levels based on ambient noisse
                    r.adjust_for_ambient_noise(source, duration=0.2)
                    talk("Ready for Commands...")
                    audio2 = r.listen(source, timeout=5)
                    
                    MyText = r.recognize_google(audio2)
                    talk(MyText)
                    return MyText

                #if there is an issue, just the function again
                except Exception as e:
                    talk(f"An error occurred: {e}")
                    talk("I didn't Understand. Try Again...")
                    r = sr.Recognizer()
                    continue
                
        except Exception as e:
            r = sr.Recognizer()
            continue

def output_text(text):
    #give name for txt, if name exists, append it if not make a new one a write to it
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return

def jasmineLoop():
    acceptingCommands = True
    #global shortcut1Open

    while(acceptingCommands):
        talk("running...")

        text = record_text()

        #need a command to open file explorer
        if(text == "add new command"):
            add_command()

        if(text == "goodbye"):
            talk("Have a good day!")
            quit()

        #check if the user is trying to open/close a shortcut
        for x in range(5):
            open_file_from_shortcut(text, x)
            close_file_from_shortcut(text, x)
       
        #output_text(text)
