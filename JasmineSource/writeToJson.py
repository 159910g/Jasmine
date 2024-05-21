import json

def write(index, path1, path2, command):
    with open('paths.json') as file:
        paths = json.load(file)

    paths[index]["primary_path"] = path1
    paths[index]["secondary_path"] = path2
    paths[index]["command"] = command

    with open('paths.json', 'w') as file:
        json.dump(paths, file, indent=4)

    print("Command Saved!")