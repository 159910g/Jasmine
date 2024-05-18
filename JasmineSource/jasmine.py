import speech_recognition as sr
import pyaudio
import pyttsx3
import os
import subprocess

r = sr.Recognizer()

def record_text():

    while(1):
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                print("Ready for Commands...")
                try:
                    audio2 = r.listen(source, timeout=5)
                    
                    MyText = r.recognize_google(audio2)
                    print(MyText)
                    return MyText

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
radred_process = None
radred_path = (r'c:\Users\zacgo\Desktop\New Radical Red\1636 - Pokemon Fire Red (U)(Squirrels) (patched).gba')
gba_path = (r'C:\Program Files\mGBA\mGBA.exe')

while(1):
    print("running...")
    text = record_text()
    if(text == "open radical red"):
        if(radred_process is None):
            print("Opening Radical Red...")
            radred_process = subprocess.Popen([gba_path, radred_path])
        else:
            print("Radical Red is Already Open...")

    if(text == "close radical red"):

        if radred_process is not None:
            print("Closing Radical Red...")
            radred_process.terminate()
            radred_process = None
        else:
            print("Radical Red Was Not Open...")

    output_text(text)
