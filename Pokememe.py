# Imports
from time import sleep
import random

# List of all pokememe + stats
#                                                                           A  H     T1          T2                   R                                      L
pokememe = {"Dwayne The Rock Johnson":  [5, 5, "Rock", "Ground", "Legendary", "If you smell what The Rock is cooking"],
              "Jolanda": [2.5, 5, "Normal", "", "Starter", "Tady vidím velký špatný"],
              "Kluk S Kamením": [4, 3, "Rock", "", "Starter", "Já jsem si přišel hrát s kamením"],
              "SirYakari": [3, 3, "Fire", "Water", "Starter", "Dobrý den dámy a pánové"],
              "Mr Beast":  [4, 4, "Normal",  "Electric", "Common", "Mr Mr Mr Beast, Mr Mr Mr Beast"],
              "Mr Bean": [4, 3, "Normal", "", "Common", "TEDDY!"],
              "Resistor-Chan": [3, 3, "Electric",  "Metal", "Common", "OWO"],
              "Lava Chicken": [4.5, 3, "Normal", "Fire", "Common", "Lalalalava Chichichichicken"],
              "Крокодил Гена": [4, 4, "Water", "", "Rare", "Медленно минуты уплыбают в даль, встречи с ними ты уже не жди."],
              "Bridget": [4, 4, "Normal", "", "Mythic", "Whoever you are, welcome to the show!"],
              "Terminator": [4.5, 4, "Metal", "", "Common",'"I will be back"'],
              "Krteček": [3.5, 4.5, "Normal", "Ground", "Hehehe"]}

# List of pokememe names, because the one you get with a method is crap
pokememe_names = ["Dwayne The Rock Johnson", "Jolanda", "Kluk S Kamením", "SirYakari", "Mr Beast",
                 "Mr Bean", "Resistor-Chan", "Lava Chicken", "Крокодил Гена", "Bridget", "Terminator", "Krteček"]

lines_toggle = input("Do you want to have character lines turned on(y/n)?\n").strip().lower()

# Starter choice
starter = input("\nPick your starter: Jolanda(1), Kluk S Kamením(2), SirYakari(3)\n")

if starter.strip() == "1":
    starter = "Jolanda"
elif starter.strip() == "2":
    starter = "Kluk S Kamením"
else:
    starter = "SirYakari"

print(f"Congrats! {starter} is now yours!")

# Removing starter from general list of pokememe
starter_stats = pokememe.get(starter)
pokememe.pop(starter)
pokememe_names.remove(starter)

# Setup of battle loop
while input("\nDo you wish to continue(y/n)?\n").lower().strip() == "y":

    # Waits
    sleep(3)

    # All of the stats for the battle 
    opponent_pokememe =  pokememe_names[random.randint(0, len(pokememe_names) - 1)]
    opponent_pokememe_stats = pokememe.get(opponent_pokememe)
    
    your_max_health =  starter_stats[1]
    opponent_max_health = opponent_pokememe_stats[1]

    # Type advantage managing
    dmg_strength = 1
    dmg_weakness = 1
    weakness_list =  ["Normal", "Rock", "Metal", "Fire", "Water", "Electric", "Ground"]
    for i in range(len(weakness_list) - 1):
        if weakness_list[i] == starter_stats[2] or weakness_list[i] == starter_stats[3]:
            if weakness_list[i + 1] == opponent_pokememe_stats[2] or weakness_list[i + 1] == opponent_pokememe_stats[3]:
                dmg_strength -= 0.25
                dmg_weakness += 0.25
            elif weakness_list[i - 1] == opponent_pokememe_stats[2] or weakness_list[i - 1] == opponent_pokememe_stats[3]:
                dmg_strength += 0.25
                dmg_weakness -= 0.25
            else:
                dmg_strength = 1
                dmg_weakness = 1

    # Had to do this
    if starter_stats[2] == "Normal" and opponent_pokememe_stats[3]  ==  "Ground":
                dmg_strength += 0.25
                dmg_weakness -= 0.25
    
    print(f"\n\nA WILD {opponent_pokememe.upper()} APPEARS")

    if lines_toggle == "y":
        sleep(1)

        print(f'\n"{opponent_pokememe_stats[5]}"')

        sleep(1)

    outcome = "NaN"
    opponent_type  = 1

    # Start of battle
    while outcome == "NaN":

        # Attack type
        attack_type = input("\nWeak(W) attack with O.K. defence or Strong(S) attack with bad defence?\n")

        if attack_type.lower().strip() == "w":
            opponent_pokememe_stats[1] = opponent_pokememe_stats[1] - starter_stats[0] / 2 * dmg_strength  * opponent_type
            attack_type = 1
        else:
            opponent_pokememe_stats[1] = opponent_pokememe_stats[1] - starter_stats[0] * dmg_strength * opponent_type
            attack_type = 2

        print(f"\nYour pokememe's health: {starter_stats[1]}\nOpponent's pokememe health: {opponent_pokememe_stats[1]}")

        # Outcome check
        if opponent_pokememe_stats[1] <= 0:
            outcome = "win"
            break

        sleep(1)

        # Opponent behaviour
        print(f"\n{opponent_pokememe} attacks!")

        opponent_type  = random.randint(1, 2)

        starter_stats[1] = starter_stats[1] - opponent_pokememe_stats[0] / opponent_type * attack_type * dmg_weakness

        print(f"\nYour pokememe's health: {starter_stats[1]}\nOpponent's pokememe health: {opponent_pokememe_stats[1]}")

        sleep(2)

        # Outcome check
        if starter_stats[1] <= 0:
            outcome = "loss"
            break

    # Win Yay ㄟ≧◇≦ㄏ
    if outcome == "win":
        print("\nYou've won!")
        
        starter_stats[1] = your_max_health
        opponent_pokememe_stats[1] = opponent_max_health
        
        # Replacing pokememe
        replace = input("\nDo you wish to replace your current pokememe with the one defeated(y/n)?\n").lower().strip()
        if replace == "y":
            pokememe.update({starter: starter_stats})
            pokememe_names.append(starter)
            pokememe_names.remove(opponent_pokememe)
            pokememe.pop(opponent_pokememe)
            starter  = opponent_pokememe
            starter_stats = opponent_pokememe_stats
            print(f"Succesfuly replaced your pokememe with {starter}!")
    # Loss
    else:
        print("\nYou've lost")
        sleep(5)
        break
    
