#%% [markdown]

### This program is used to take in a word and return the definition/meaning of that word based on a json file

#%%
import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

#%%
#Load the json file which contains the word definitions
data=json.load(open('data.json'))

#%% [markdown]
#### Build a function which returns the word definition given a word

#%%
word=input("Enter a word: ")

def word_meaning(word):
    if word in data:
        word=word.lower()
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys(),cutoff=0.8))>0:
        yn= input("Did you mean %s instead? Enter Y if yes, N if no: " % get_close_matches(word,data.keys())[0])
        if yn=="Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=="N":
            return "The word you entered doesn't exist in the database. Please double check it."
        else:
            return "We didn't understandt your entry"
    else:
        return "The word doesn't exist. Please double check"

output=word_meaning(word)

if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
# %%
