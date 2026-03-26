import win32com.client
import time

speaker = win32com.client.Dispatch("SAPI.SpVoice")

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

def speak_and_print(text):
    print(text)          # Print first
    speaker.Speak(text)  # Then speak (BLOCKING - waits until done)

for msg in messages:
    speak_and_print(msg)
    time.sleep(0.2)      # Small pause between lines