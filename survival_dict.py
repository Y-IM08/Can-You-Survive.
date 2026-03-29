# anychanges related to labels and url will be done here.

import win32com.client
import time
import random 
import requests

url="https://api.adviceslip.com/advice"
def get_advice():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            advice = response.json()['slip']['advice']
            return advice
        else:
            return "Stay safe and be careful"
    except Exception as e:
        return f"Watch your step.{e}"
    
for i in range(10):
    advice=get_advice()
        
    word_splitter=advice.split()
    splitted_word=[w.strip(",./?:;'-_|") for w in word_splitter]

    num_to_pick=min(10,len(splitted_word))
random_word_picker=random.sample(splitted_word,num_to_pick) # random.sample return the k length of string or list whatever the format is and the first is population index

labels=["precious","poison","neutral","danger","necessary","treasure"]

survival_dict={}
print("--SURVIVAL ITEMS--")
for word in random_word_picker:
    survival_dict[word]=random.choice(labels)

print(survival_dict)