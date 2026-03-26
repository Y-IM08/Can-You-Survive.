from gtts import  gTTS
import os
import time
# rules printing
rules = [
    "Welcome to the Game",
    "Can U Survive?",
    "Rules for survival in the game: ",
    "Rule No. 1",
    "You start with a list of items that contains precious objects, poison, dangerous animals and many other things",
    "Rule No. 2",
    "Each turn, you are asked to remove an item:",
    "If you removed the correct item, you clear that round.",
    "But if you removed the wrong item, you lose, and whenever you lose, you lose one life to clear that dungeon",
    "Remember the system asks you to remove the item by pure luck, by a condition, or by logic.",
    "If you pass every round and survive all stages, you win this game",
    "But if you lose all your lives, you lose the game and the game ends."
]
# print and speak rules
for rule in rules:
    # engine=pyttsx3.init() #engine initialization
    # engine.say(rule)
    # engine.runAndWait()

    print(rule)

    tts=gTTS(text=rule,lang='en')
    tts.save('temp.mp3')

    os.system('Start/wait wmplayer temp.mp3')
    time.sleep(0.6)