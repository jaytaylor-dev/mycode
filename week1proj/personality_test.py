#!usr/bin/env python3

import 

def run_personality_test():
    questions: [{"question": "You find yourself stranded on a deserted island with only one item. What would it be?",
         "options": {"a": "A sturdy machete for cutting through vegetation",
                     "b": "A durable shelter-building kit",
                     "c": "A versatile multi-tool with various functions"}},

        {"question": "You wake up in a mysterious labyrinth with only one item. What do you choose?",
         "options": {"a": "A pair of swift and silent throwing knives",
                     "b": "A set of impenetrable force field generators",
                     "c": "A device with unknown alien functions"}},

        {"question": "While exploring a futuristic city, you stumble upon a hidden chamber. What item do you take with you?",
         "options": {"a": "A futuristic energy blaster with precision targeting",
                     "b": "A suit with advanced camouflage technology",
                     "c": "A holographic interface device with unidentified abilities"}}, 
         ]

    tally = 0

    for question in questions:
        print(question["question"])
        for option, description in question["options"].items():
            print(f"{option}: {description}")

        user_answer = input("Your answer: ").lower()

        if user_answer in question["options"]:
            tally += calculate_tally_total(
