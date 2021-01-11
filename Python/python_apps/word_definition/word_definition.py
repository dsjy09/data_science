#%% [markdown]

### This program is used to take in a word and return the definition/meaning of that word based on a json file

#%%
import json
import difflib
from difflib import SequenceMatcher

#%%
#Load the json file which contains the word definitions
data=json.load(open('data.json'))

#%% [markdown]
#### Build a function which returns the word definition given a word

#%%
word=input("Enter a word: ")

#%%
def word_meaning(word):
    if word in data:
        word=word.lower()
        return data[word]
    else:
        return "The word doesn't exist. Please double check"

print(word_meaning(word))
# %%
