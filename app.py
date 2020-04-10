import json
from difflib import get_close_matches

data = json.load(open("data.json")) 

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        given_word = get_close_matches(w, data.keys())[0]
        yn = input(f"Did you mean {given_word}, Enter Y if yes N if no. ")
        if yn == "Y":
            return data[given_word]
        elif yn == "N":
            return "Please double check"
        else:
            return "Please only enter Y or N."
    else:
        return "Word doesn't exist. Please double check"

word = input("Please enter a word: ")

output = (translate(word))

if type(output) == list:
    for i in output:
        print(f"\n {i} \n")
else:
    print(output)

