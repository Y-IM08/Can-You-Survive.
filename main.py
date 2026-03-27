import win32com.client
import time
import random 
import requests
narrator=win32com.client.Dispatch("SAPI.SpVoice")
rules = [
    "Welcome to the Game",
    "Can You Survive?",
    "Rules for survival in the game:",
    "Rule Number 1",
    "You start with a list of items that contains precious objects, poison, dangerous animals and many other things",
    "Rule Number 2",
    "Each turn, you are asked to remove an item:",
    "If you removed the correct item, you clear that round.",
    "But if you removed the wrong item, you lose, and whenever you lose, you lose one life to clear that dungeon",
    "Remember the system asks you to remove the item by pure luck, by a condition, or by logic.",
    "If you pass every round and survive all stages, you win this game",
    "But if you lose all your lives, you lose the game and the game ends."
]
def speak_and_print(text):
    print(text)
    narrator.Speak(text)

for r in rules:
    speak_and_print(r)
    time.sleep(0.25)
 

url="https://api.adviceslip.com/advice"
def get_advice():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            advice = response.json()['slip']['advice']
            return advice
        else:
            return "Could not fetch advice at the moment."
    except Exception as e:
        return f"An error occurred: {e}"
    
for i in range(10):
    advice_dict={f"advice_{i}" : get_advice()}
    # advice=int(input(get_advice()))

    
    
# for i in range(10):
    # advice=int(input(get_advice()))
    # advice_dict=

    print(advice_dict)