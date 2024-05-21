import json
import os
import jasmine

def startupCheck():
    if os.path.isfile("paths.json") and os.access("paths.json", os.R_OK):
        # checks if file exists
        print ("File exists and is readable")
    else:
        print ("Either file is missing or is not readable, creating file...")

        template = [
            {
                "primary_path": "",
                "secondary_path" : "",
                "command" : ""
            },
            {
                "primary_path": "",
                "secondary_path" : "",
                "command" : ""
            },
            {
                "primary_path": "",
                "secondary_path" : "",
                "command" : ""
            },
            {
                "primary_path": "",
                "secondary_path" : "",
                "command" : ""
            },
            {
                "primary_path": "",
                "secondary_path" : "",
                "command" : ""
            }
        ]
        
        json_string = json.dumps(template, indent=4)
        with open('paths.json', 'w') as outfile:  
            outfile.write(json_string)
    
    jasmine.jasmineLoop()

    

startupCheck()