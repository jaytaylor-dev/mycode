#!usr/bin/env python3
from char_challenge_dict import marvelchars


char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)\n")

if char_name.capitalize() in marvelchars:
    print(f"You chose {char_name.capitalize()}\n")
else:
    print(f"Sorry, {char_name.capitalize()} is not in our dictionary. Printing dictionary: \n")
    print(marvelchars)

char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)\n")

if char_stat.lower() in marvelchars[char_name.capitalize()]:
    print(f"You want to learn their: {char_stat.lower()}")
    print(f"{char_name.capitalize()}'s {char_stat.lower()} is: {marvelchars[char_name.capitalize()][char_stat.lower()]}")
