import win32com.client
import time
import random 
import requests
# narrator=win32com.client.Dispatch("SAPI.SpVoice")
# rules = [
#     "Welcome to the Game",
#     "Can You Survive?",
#     "Rules for survival in the game:",
#     "Rule Number 1",
#     "You start with a list of items that contains precious objects, poison, dangerous animals and many other things",
#     "Rule Number 2",
#     "Each turn, you are asked to remove an item:",
#     "If you removed the correct item, you clear that round.",
#     "But if you removed the wrong item, you lose, and whenever you lose, you lose one life to clear that dungeon",
#     "Remember the system asks you to remove the item by pure luck, by a condition, or by logic.",
#     "If you pass every round and survive all stages, you win this game",
#     "But if you lose all your lives, you lose the game and the game ends."
# ]
# def speak_and_print(text):
#     print(text)
#     narrator.Speak(text)

# for r in rules:
#     speak_and_print(r)
#     time.sleep(0.1)
 

# url="https://api.adviceslip.com/advice"
# def get_advice():
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             advice = response.json()['slip']['advice']
#             return advice
#         else:
#             return "Stay safe and be careful"
#     except Exception as e:
#         return f"Watch your step.{e}"
    
# for i in range(10):
#     advice=get_advice()
        
#     word_splitter=advice.split()
#     splitted_word=[w.strip(",./?:;'-_|") for w in word_splitter]

#     num_to_pick=min(10,len(splitted_word))
# random_word_picker=random.sample(splitted_word,num_to_pick) # random.sample return the k length of string or list whatever the format is and the first is population index

# labels=["precious","poison","neutral","danger","necessary","treasure"]

# survival_dict={}
# print("--SURVIVAL ITEMS--")
# for word in random_word_picker:
#     survival_dict[word]=random.choice(labels)

# print(survival_dict)
# player=input("Enter your choosen word: ")










