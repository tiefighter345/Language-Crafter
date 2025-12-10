import json


def new_language():
    name = input("What is the name of your language?\n>")
    data = {
        "name": name
        }
    with open(f'languages/{name}.json', 'w') as language:
        json.dump(data, language)

def edit_langauge():
    print("Editing langauge")

def Main():
    print("Welcome to Language Crafter!")

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
        edit_langauge()

    print("Goodbye")

if __name__ == "__main__":
    Main()