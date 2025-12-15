#IMPORTS
import json
from os import listdir, makedirs, system
from os.path import isfile, join, isdir
from platform import system as os_check

clear = ""
#Check which os is being used for correct clearing of the terminal
def check_os():
    if os_check() == "Windows":
        clear = "cls"
    elif os_check() == "Darwin" or os_check() == "Linux":
        clear = "clear"
    
    return clear

#Load language
def select_langauge():
    #Display available languages
    languages = [f for f in listdir("Languages") if isfile(join("Languages", f))]
    if len(languages) != 0:
        print("Available languages:")
        for i in range(len(languages)):
            l = languages[i].split(".")[0]
            print(f"{i+1}: {l}")
        
        flag1 = True
        flag2 = True
        print("Which language do you want to load? (number)")
        
        #exception catching loop
        while flag1:        
            while flag2:
                selector = input(">")
                try: selector = int(selector)
                except: 
                    print("input a valid number")
                else: flag2 = False

            if selector <= 0 or selector > len(languages):
                print("input a valid number")
                flag2 = True
            else:
                flag1 = False
                selector -= 1
        
        #open language folder
        with open(f"Languages/{languages[selector]}", "r") as data:
            language_data = json.load(data)
            language_name = language_data["name"]
        
        system(clear)
        print(f"you selected '{language_name}'")
        return language_data
    
    else: 
        print("There are no existing languages")
        return None


#Save language data
def save_language(data):
    name = data["name"]
    with open(f'languages/{name}.json', 'w') as language:
        json.dump(data, language)


#Create a new language
def new_language():
    #name of the language
    name = input("What is the name of your language? (or type 'exit' to cancel)\n>")
    
    #saving the name to the language folder
    if name != "exit":
        data = {
            "name": name,
            "words": []
            }
        
        save_language(data)
        system(clear)
        print("Language created\n\n")
    
    else: system(clear)


#Edit an existing language
def edit_language():
    language = select_langauge()
    if language == None: return
    
    looping = True
    while looping:
        #edit input
        flag = True
        print("'n' to add a new word, 'd' to delete an existing pair, 'exit' to go back to main menu")
        while flag:
            edit_action = input(">")
            if edit_action != "n" and edit_action != "d" and edit_action != "exit":
                print("Type a valid input (n or d or exit)")
            else: flag = False

        #add new word
        if edit_action == "n":
            print("What is the word in your language? (or type exit to cancel)")
            word = input(">")
            
            if word != "exit":
                print("What is the word in English")
                translation = input(">")

                new_data = [word, translation]

                language["words"].append(new_data)
        
        #delete an existing word
        elif edit_action == "d":
            #load and display pairs
            words = language["words"]
            for i in range(len(words)):
                pair = words[i]
                print(f"{i+1}: {pair[0]}, translating to: {pair[1]}")
            print("Which pair do you want to delete? (number) or 'exit to exit")
            
            #exception catching loop
            flag1 = True
            flag2 = True
            while flag1:        
                while flag2:
                    selector = input(">")
                    if selector != "exit":
                        try: selector = int(selector)
                        except: 
                            print("input a valid number")
                        else: flag2 = False
                if selector != "exit":
                    if selector <= 0 or selector > len(words):
                        print("input a valid number")
                        flag2 = True
                    else:
                        flag1 = False
                        selector -= 1
            
            #delete chosen pair
            if word != "exit":
                words.pop(selector)

        
        #exit the loop
        else:
            looping = False


    save_language(language)


def Main():
    print("Welcome to Language Crafter!")
    
    #Check for Languages folder
    if not isdir("Languages"):
        makedirs("Languages")

    check_os()

    #main loop
    running = True
    while running:
        flag = True
        print("'n' to add a new language, 'e' to edit an existing one, 'exit' to exit")
        while flag:
            user_input = input(">")
            if user_input == "e" or user_input == "n" or user_input == "exit":
                flag = False
            else:
                print("please input a valid answer (n for new or e for edit, 'exit' to exit)")

        system(clear)
        if user_input == "n":
            new_language()
        elif user_input == "e":
            edit_language()
        else: running = False

    print("Goodbye")

if __name__ == "__main__":
    Main()