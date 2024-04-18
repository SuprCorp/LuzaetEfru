import webbrowser
import os
import csv
import json
import time

# Dictionary to map aliases to their corresponding paths
aliases = {
    "settings": "ms-settings:system",
    "calculator": "calc.exe",
    "notepad": "notepad.exe",
    "calendar": "outlookcal:",
    "photos": "ms-photos:",
    "xbox": "xbox:",
    "clock": "ms-clock:",
    "microsoft edge": "microsoft-edge:",
    "edge": "microsoft-edge:",
    "microsoft store": "ms-windows-store:",
    "store": "ms-windows-store:",
    "camera": "microsoft.windows.camera:",
    "paint": "ms-paint:",
    "paint 3d": "ms-paint:",
    "weather": "bingweather:",
    "maps": "bingmaps:",
    "minecraft": "minecraft:",
    "mail": "outlookmail:",
    "help": "ms-contact-support:",
    "command": "cmd.exe",
    "files": "explorer.exe",
    "file explorer": "explorer.exe",
    "google chrome": "chrome.exe",
    "google": "chrome.exe",
    # Add more aliases here
}

# Function to open a URL in a web browser
def open_url(url):
    webbrowser.open(url)

# Function to open a specific program or file
def open_program_or_file(name):
    try:
        if name.endswith(".exe"):
            os.startfile(name)
            print("I just opened " + name + " for you.")
        elif name.endswith((".txt", ".docx", ".pdf")):
            os.system("start " + name)
            print("I just opened the file called " + name + " for you.")
        else:
            if name in aliases:
                os.startfile(aliases[name])
                print("I just opened " + name + " for you.")
            else:
                print("Sorry, I can't open that file or program.")
                time.sleep(0.5)
                print("But I will try to append .exe to it for you.")
                time.sleep(1)
                os.startfile(name + ".exe")
    except FileNotFoundError:
        print("Sorry, I couldn't find the file or program.")

# Function to create a text file with given content
def create_file(filename, content, file_type):
    if file_type == "text":
        with open(filename + ".txt", 'w') as file:
            file.write(content)
            print("I just created " + filename + " for you.")
    elif file_type == "csv":
        with open(filename + ".csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(content.split(','))
            print("I just created " + filename + " for you.")
    elif file_type == "json":
        data = json.loads(content)
        with open(filename + ".json", 'w') as file:
            json.dump(data, file, indent=4)
            print("I just created " + filename + " for you.")
    else:
        print("Sorry.. Unsupported file type.")

# Function to create a directory
def create_directory(directory_name):
    os.makedirs(directory_name)
    print("I just created the directory called " + directory_name + " for you.")

# Function to rename a file
def rename_file(old_name, new_name):
    os.rename(old_name, new_name)
    print("I just renamed " + old_name + " to " + new_name + " for you.")

# Function to delete a file
def delete_file(filename):
    os.remove(filename)
    print("I just deleted " + filename + " for you.")

# Function to list contents of a directory
def list_directory_contents(directory="."):
    contents = os.listdir(directory)
    print("Sure, I will list all files in the directory called " + directory + " for you.")
    for item in contents:
        print(item)

# Function to search the web
def search_web(query):
    url = "https://www.google.com/search?q=" + query.replace(" ", "+")
    open_url(url)
    print("I just searched " + query + " for you.")

# Function to perform different tasks based on user input
def perform_task(task):
    if any(keyword in task for keyword in ["open", "launch"]):
        item = task.split(maxsplit=1)[-1].strip()
        if item.startswith("http://") or item.startswith("https://"):
            open_url(item)
        else:
            open_program_or_file(item)
    elif any(keyword in task for keyword in ["search", "look up"]):
        query = task.split(maxsplit=1)[-1].strip()
        search_web(query)
    elif "create a text file called" in task:
        parts = task.split("with contents saying")
        filename = parts[0].replace("create a text file called", "").strip()
        content = parts[1].strip()
        create_file(filename, content, "text")
    elif "create a csv file called" in task:
        parts = task.split("with contents as")
        filename = parts[0].replace("create a csv file called", "").strip()
        content = parts[1].strip()
        create_file(filename, content, "csv")
    elif "create a json file called" in task:
        parts = task.split("with contents as")
        filename = parts[0].replace("create a json file called", "").strip()
        content = parts[1].strip()
        create_file(filename, content, "json")
    elif "create a directory called" in task:
        directory_name = task.split("create a directory called", 1)[-1].strip()
        create_directory(directory_name)
    elif "rename file" in task:
        parts = task.split("to")
        old_name = parts[0].replace("rename file", "").strip()
        new_name = parts[1].strip()
        rename_file(old_name, new_name)
    elif "delete file" in task:
        filename = task.replace("delete file", "").strip()
        delete_file(filename)
    elif "list contents of directory" in task:
        directory = task.replace("list contents of directory", "").strip()
        list_directory_contents(directory)
    elif "exit" in task:
        print("Goodbye!")
        exit()
    else:
        print("Sorry, I didn't understand that command.")

# Main function
def main():
    print("Welcome to Luzaet Efru, your go-to Task Doer!")
    print("Please type your command or 'exit' to quit.")

    while True:
        user_input = input(">> ").lower()
        perform_task(user_input)

if __name__ == "__main__":
    main()
