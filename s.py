import subprocess
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

def speak(text):
    subprocess.call([
        'powershell', '-Command',
        f'Add-Type -AssemblyName System.Speech; '
        f'$s=New-Object System.Specch.Synthesis.SpecchSynthesizer; '
        f'$s.speak("{text}")'
    ])

for rule in rules:
    print(rule)
    speak(rule)    