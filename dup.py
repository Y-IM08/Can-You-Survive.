# import pyttsx3

# engine = pyttsx3.init()

# engine.say("Welcome to the Game")
# engine.runAndWait()
# print("Welcome to the Game")

# engine.say("Can You Survive?")
# engine.runAndWait()
# print("Can You Survive?")

# rules = [
#     "Rules for survival in the game: ",
#     "Rule No. 1",
#     "You start with a list of items that contains precious objects, poison, dangerous animals and many other things",
#     "Rule No. 2",
#     "Each turn, you are asked to remove an item:",
#     "If you removed the correct item, you clear that round.",
#     "But if you removed the wrong item, you lose, and whenever you lose, you lose one life to clear that dungeon",
#     "Remember the system asks you to remove the item by pure luck, by a condition, or by logic.",
#     "If you pass every round and survive all stages, you win this game",
#     "But if you lose all your lives, you lose the game and the game ends."
# ]

# for rule in rules:
#     engine.say(rule)
#     engine.runAndWait()
#     print(rule)
import pyttsx3
import time

# Initialize the engine
engine = pyttsx3.init()

# Messages to speak and print
messages = [
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


def speak(text):

    # print()  
    engine.stop()        # Print to console
    engine.say(text)     # Speak the message
    engine.runAndWait() # Execute speaking
    time.sleep(0.5)

for msg in messages:
    print(msg)
    speak(msg)




# engine.say("hi")
# engine.runAndWait()

    