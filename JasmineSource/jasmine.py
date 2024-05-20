import speech_recognition as sr
import pyaudio
import pyttsx3
import os
import subprocess
import json

r = sr.Recognizer()

def record_text():

    while(1):
        try:
            #tell jasmine to use the microphone
            with sr.Microphone() as source:
                #adjust audio levels based on ambient noisse
                r.adjust_for_ambient_noise(source, duration=0.2)
                print("Ready for Commands...")
                try:
                    audio2 = r.listen(source, timeout=5)
                    
                    MyText = r.recognize_google(audio2)
                    print(MyText)
                    return MyText

                #if there is an issue, just the function again
                except Exception as e:
                    print(f"An error occurred: {e}")
                    print("I didn't Understand. Try Again...")
                    r = sr.Recognizer()
                    continue
                
        except Exception as e:
            r = sr.Recognizer()
            continue

def output_text(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return

#while loop means its always listening
#radred_path = (r'c:\Users\zacgo\Desktop\New Radical Red\1636 - Pokemon Fire Red (U)(Squirrels) (patched).gba')
#gba_path = (r'C:\Program Files\mGBA\mGBA.exe')

def jasmineLoop():
    radred_process = None
    while(1):
        print("running...")

        text = record_text()

        #need a command to open file explorer

        #open file
        if(text == "open radical red"):
            if(radred_process is None):
                print("Opening Radical Red...")
                #read paths from the json file
                with open('paths.json') as file:
                    paths = json.load(file)
                radred_process = subprocess.Popen([paths["primary_path"], paths["secondary_path"]])
            else:
                print("Radical Red is Already Open...")

        #close file
        if(text == "close radical red"):

            if radred_process is not None:
                print("Closing Radical Red...")
                radred_process.terminate()
                radred_process = None
            else:
                print("Radical Red Was Not Open...")

        output_text(text)
