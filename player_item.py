player_choice=input("/n Pick an word to remove from your dictionary to go to next level: ").strip().lower()
if player_choice in survival_dict:
    status= survival_dict[player_choice]
    print(f"You picked : {player_choice}")      
    print(f"This item in {player_choice} is {status} removed from survival_dict")

    if status in ["poison","danger"]:
        speak_and_print(f"Since you have choosen the {status}, your life decreases by -1.")
        speak_and_print(f"Choose next time wisely.")

    elif status in ["precious","treasure"]:
        speak_and_print(f"Since you have choosen the {status}, your score increases by +50.")
        speak_and_print("Good! keep it up.")

    elif status in ["neutal"]:
        speak_and_print("You are safe this time.")

    elif status in ["necessary"]:
        speak_and_print(f"You Picked {status} item this time.")
        speak_and_print(f"Do not pick it again otherwise you lose your life.") 

    else:
        speak_and_print(f"Your Choosen item {player_choice} is not present.")








