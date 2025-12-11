#IMPORTS
import json
from os import listdir, makedirs
from os.path import isfile, join, isdir

#Load language
def load_langauge():
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
        
        print(f"you selected '{language_name}'")
        return language_data
    
    else: 
        print("There are no existing languages")
        return None


#Create a new language
def new_language():
    #name of the language
    name = input("What is the name of your language?\n>")
    
    #saving the name to the language folder
    data = {
        "name": name,
        "words": []
        }
    
    save_language(data)
    

#Save language data
def save_language(data):
    name = data["name"]
    with open(f'languages/{name}.json', 'w') as language:
        json.dump(data, language)

#Edit an existing language
def edit_language():
    language = load_langauge()
    if language == None: return

    #edit type
    flag = True
    print("what type of edit do you want to do? (n for add word, d for delete word)")
    while flag:
        edit_action = input(">")
        if edit_action != "n" and edit_action != "d":
            print("Type a valid input (n for add new ford or d for delete existing word)")
        else: flag = False

    #add new word
    if edit_action == "n":
        print("What is the word in your language?")
        word = input(">")

        print("What is the word in English")
        translation = input(">")

        new_data = [word, translation]

        language["words"].append(new_data)
    
    #delete an existing word
    else:
        #load and display pairs
        words = language["words"]
        for i in range(len(words)):
            pair = words[i]
            print(f"{i+1}: {pair[0]}, translating to: {pair[1]}")
        print("Which pair do you want to delete? (number)")
        
        #exception catching loop
        flag1 = True
        flag2 = True

        while flag1:        
            while flag2:
                selector = input(">")
                try: selector = int(selector)
                except: 
                    print("input a valid number")
                else: flag2 = False

            if selector <= 0 or selector > len(words):
                print("input a valid number")
                flag2 = True
            else:
                flag1 = False
                selector -= 1
        
        #delete chosen pair
        words.pop(selector)


    save_language(language)


def Main():
    print("Welcome to Language Crafter!")
    
    #Check for Languages folder
    if not isdir("Languages"):
        makedirs("Languages")

    flag = True
    print("Do you want to create a new language or edit an exist one? (n for new or e for edit)")
    while flag:
        user_input = input(">")
        if user_input == "e" or user_input == "n":
            flag = False
        else:
            print("please input a valid answer (n for new or e for edit)")

    if user_input == "n":
        new_language()
    else:
        edit_language()


    print("Goodbye")

if __name__ == "__main__":
    Main()