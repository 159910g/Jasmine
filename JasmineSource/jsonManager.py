import json
import os
import jasmine

def startupCheck():
    if os.path.isfile("paths.json") and os.access("paths.json", os.R_OK):
        # checks if file exists
        print ("File exists and is readable")
    else:
        print ("Either file is missing or is not readable, creating file...")
        with open('paths.json', 'w') as outfile:  
            outfile.write('{}')
    
    jasmine.jasmineLoop()

    

startupCheck()