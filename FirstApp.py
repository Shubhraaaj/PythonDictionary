import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))
status = True
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        closestword = get_close_matches(word, data.keys())[0]
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " %closestword)
        if yn == "Y":
            return data[closestword]
        elif yn == "N":
            return "The word doesn't exists. Please recheck it"
        else:
            return "Wrong option entered"
    else:
        return "The word doesn't exists. Please recheck it"

while(status):
    word = input("Enter word: ")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
    option = input("\nEnter 1 to search again, or 2 to exit: ")
    if option == "1":
        status = True
    elif option == "2":
        status = False
    else:
        print("Wrong input! Exiting program...")
        status = False