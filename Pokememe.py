# Spacing/variable laws in order of importance:

# Comments are ignored

# Defs have 2 blank lines surrounding them
# Ifs have 1 blank line surrounding them

# No more than 5 non-blank lines are allowed (except for dictionaries and lists)

# Vars' names established OUTSIDE of defs: normal
# Vars' names established IN defs: Have 1 letter at the end of a word per var REMOVED

# Imports
from time import sleep
import random

# List of all pokememe + stats
#                                                                            A  H     T1          T2                   R                                      L
pokememe: dict = {"Dwayne The Rock Johnson":  [4.5, 6, "Rock", "Ground", "Legendary", "If you smell what The Rock is cooking"],
              "Jolanda": [2.5, 6, "Normal", "", "Starter", "Tady vidím velký špatný"],
              "Kluk S Kamením": [3.5, 4, "Rock", "", "Starter", "Já jsem si přišel hrát s kamením"],
              "SirYakari": [3, 4, "Fire", "Water", "Starter", "Dobrý den dámy a pánové"],
              "Mr Beast":  [3.5, 4.75, "Normal",  "Electric", "Common", "Mr Mr Mr Beast, Mr Mr Mr Beast"],
              "Mr Bean": [4, 4, "Normal", "", "Common", "TEDDY!"],
              "Resistor-Chan": [3, 4, "Electric",  "Metal", "Common", "OWO"],
              "Lava Chicken": [4, 4, "Normal", "Fire", "Common", "Lalalalava Chichichichicken"],
              "Крокодил Гена": [3.75, 5, "Water", "", "Rare", "Медленно минуты уплыбают в даль, встречи с ними ты уже не жди."],
              "Bridget": [4, 5, "Normal", "Yoyo", "Mythic", "Whoever you are, welcome to the show!"],
              "Terminator": [3.5, 5, "Metal", "", "Rare","I will be back"],
              "Krteček": [3, 4.5, "Normal", "Ground",  "Common", "Hehehe"]}

# Note: There is no "Yoyo" type included anywhere else in the code. This is intetional

# List of pokememe names, because the one you get with the method is crap
pokememe_names: list = ["Dwayne The Rock Johnson", "Jolanda", "Kluk S Kamením", "SirYakari", "Mr Beast",
                 "Mr Bean", "Resistor-Chan", "Lava Chicken", "Крокодил Гена", "Bridget", "Terminator", "Krteček"]

# Vars 
xp: int = 0


###################
# FUNCTIONS HERE#
###################


def StarterChoice(star):

    # star == starter
    if star.strip() == "1":
        star = "Jolanda"
        
    elif star.strip() == "2":
        star = "Kluk S Kamením"
        
    else:
        star = "SirYakari"

    print(f"Congrats! {star} is now yours!")

    return star


def TypeAdvantageManaging(star_stats, opponen_pokememe_stats):
    
    # Stat establishment
    dmg_strengt: int = 1
    dmg_weaknes: int = 1
    weakness_list: list =  ["Normal", "Rock", "Metal", "Fire", "Water", "Electric", "Ground"]

    # Spaghetti, yummy!
    for i in range(len(weakness_list) - 1):
        
        if weakness_list[i] == star_stats[2] or weakness_list[i] == star_stats[3]:
            
            if weakness_list[i + 1] == opponen_pokememe_stats[2] or weakness_list[i + 1] == opponen_pokememe_stats[3]:
                dmg_strengt -= 0.25
                dmg_weaknes += 0.25
                
            elif weakness_list[i - 1] == opponen_pokememe_stats[2] or weakness_list[i - 1] == opponen_pokememe_stats[3]:
                dmg_strengt += 0.25
                dmg_weaknes -= 0.25
                
            else:
                dmg_strengt = 1
                dmg_weaknes = 1
                
    # Had to do this (well, actually no, but you get the point)
    if star_stats[2] == "Normal" and opponen_pokememe_stats[3]  ==  "Ground":
                dmg_strengt += 0.25
                dmg_weaknes -= 0.25

    return [dmg_strengt, dmg_weaknes]


def YourAttack(opponen_pokememe_stats, star_stats, dmg_strengt, opponen_type):
        
        # Attack type
        attack_typ: str = input("\nWeak(W) attack with O.K. defence or Strong(S) attack with bad defence?\n")

        # Decides what to do
        if attack_typ.lower().strip() == "w":
            opponen_pokememe_stats[1] = opponen_pokememe_stats[1] - star_stats[0] / 2 * dmg_strength  * opponen_type
            attack_typ = 1
            
        else:
            opponen_pokememe_stats[1] = opponen_pokememe_stats[1] - star_stats[0]  * dmg_strength * opponen_type
            attack_typ = 2

        opponen_pokememe_stats[1] = round(opponen_pokememe_stats[1], 2)

        return attack_typ


def XpHandling(opponen_pokememe_stats):

    # Just learned that python has no switch statements (I don't personally think implementing it in another way is clean) :(
        # A.K.A. xp management
        rarity: str = opponen_pokememe_stats[4]
        exp: int = 0
        
        if rarity == "Starter" or rarity == "Common":
            exp += 10
            
        elif rarity == "Rare":
            exp += 20

        elif rarity == "Mythic":
            exp += 40

        else:
            exp += 75

        return exp


#########################
# FUNCTIONS STOP HERE#
#########################


# Starting stuff
lines_toggle: str = input("Do you want to have character lines turned on(y/n)?\n").strip().lower()

starter: str = input("\nPick your starter: Jolanda(1), Kluk S Kamením(2), SirYakari(3)\n")
starter = StarterChoice(starter)

# Removing starter from general list of pokememe
starter_stats = pokememe.get(starter)

pokememe.pop(starter)
pokememe_names.remove(starter)

# Setup of battle loop
while input("\nDo you wish to continue(y/n)?\n").lower().strip() == "y":

    # Waits
    sleep(3)

    # All of the stats for the battle 
    opponent_pokememe: str =  pokememe_names[random.randint(0, len(pokememe_names) - 1)]
    opponent_pokememe_stats: list = pokememe.get(opponent_pokememe)
    
    your_max_health: int =  starter_stats[1]
    opponent_max_health: int = opponent_pokememe_stats[1]

    # Type advantage managing
    strength_weakness: list = TypeAdvantageManaging(starter_stats, opponent_pokememe_stats)
    
    dmg_strength: int = strength_weakness[0]
    dmg_weakness: int = strength_weakness[1]
    
    print(f"\n\nA WILD {opponent_pokememe.upper()} APPEARS")

    if lines_toggle == "y":
        sleep(1)

        print(f'\n"{opponent_pokememe_stats[5]}"')

        sleep(1)

    sleep(1)
    
    print(f"\nYour pokememe's health: {starter_stats[1]}\nOpponent's pokememe health: {opponent_pokememe_stats[1]}")

    sleep(1)
    
    outcome: str = "NaN"
    opponent_type: int  = 1

    # Start of battle
    while outcome == "NaN":

        # Your turn
        attack_type: int = YourAttack(opponent_pokememe_stats, starter_stats, dmg_strength, opponent_type)

        if opponent_pokememe_stats[1] < 0:
            opponent_pokememe_stats[1] = 0

        print(f"\nYour pokememe's health: {starter_stats[1]}\nOpponent's pokememe health: {opponent_pokememe_stats[1]}")
        
        # Outcome check
        if opponent_pokememe_stats[1] <= 0:
            outcome = "win"
            break

        sleep(1)

        # Opponent behaviour
        print(f"\n{opponent_pokememe} attacks!")

        opponent_type: int  = random.randint(1, 2)
        
        starter_stats[1] = starter_stats[1] - opponent_pokememe_stats[0] * opponent_type * attack_type / 2 * dmg_weakness
        starter_stats[1] = round(starter_stats[1], 2)

        # Makes it so your hp is never below 0
        if starter_stats[1] < 0:
            starter_stats[1] = 0
            
        print(f"\nYour pokememe's health: {starter_stats[1]}\nOpponent's pokememe health: {opponent_pokememe_stats[1]}")

        sleep(2)

        # Outcome check
        if starter_stats[1] <= 0:
            outcome = "loss"
            break

    # Win Yay ㄟ≧◇≦ㄏ
    if outcome == "win":
        print("\nYou've won!")

        xp += XpHandling(opponent_pokememe_stats)
            
        starter_stats[1] = your_max_health
        opponent_pokememe_stats[1] = opponent_max_health
        
        # Replacing pokememe - LONG
        replace: str = input("\nDo you wish to replace your current pokememe with the one defeated(y/n)?\n").lower().strip()

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
        
        sleep(2.5)
        
        break

print(f"\nYour score: {xp}")

sleep(5)
