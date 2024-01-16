# personality_test.py
#!usr/bin/env python3

print(f"Good day, Today I will be checking your aptitude. Please do not think to hard about the questions.\n")
input("Hit enter to continue: ")
def run_personality_test():
    questions = [
        {"question": "You find yourself stranded on a deserted island with only one item. What would it be?",
         "options": {"a": "A sturdy machete for cutting through vegetation",
                     "b": "A durable shelter-building kit",
                     "c": "A versatile multi-tool, (swiss-knife)"}},

        {"question": "You wake up in a mysterious labyrinth with only one item. What do you choose?",
         "options": {"a": "A pair of swift and silent throwing knives",
                     "b": "A set of impenetrable force field generators",
                     "c": "An alien device that emits a warm healing glow"}},

        {"question": "While exploring a futuristic city, you stumble upon a hidden chamber. What item do you take with you?",
         "options": {"a": "A futuristic energy blaster with precision targeting",
                     "b": "A suit with advanced nano-armor",
                     "c": "A holographic pair of glasses with biometric scanning "}},
        {"question": "In a dark room you hear something burst into the door what do you grab first?", 
         "options": {"a": "Your trusty bat, thats always by your side",
                     "b": "The family crested shield, its always in arms reach",
                     "c": "A flashlight, no one would want to hurt you its probably a friend"}}

    ]

    points = 0

    for question in questions:
        print(question["question"])
        for option, description in question["options"].items():
            print(f"{option}: {description}")

        user_answer = input("Your choice: ").lower()

        if user_answer in question["options"]:
            points += calculate_points(user_answer)

    result = classify_result(points)
    print(f"Your personality test result: {result}")

def calculate_points(answer):
    # point system chmod-esque

    if answer == "a":
        # DPS
        return 3
    elif answer == "b":
        #  Tank
        return 2
    elif answer == "c":
        #  Support
        return 1
    else:
        # Handle invalid input
        print("Invalid choice. No points awarded.")
        return 0

def classify_result(total_points):
    # simple calculation of points from results
    # NOTE: for each question added 
    if total_points >= 11:
        return "Pretty aggressive, you should be a dps!"
    elif total_points == 10:
        return "A dps hybrid! UNIQUE!"
    elif 6 < total_points <= 8:
        return "You seems to be sturdy!, consider tanking!"
    elif total_points == 6:
        return "A healer hybrid! ELITE"
    elif total_points == 5:
        return "You seem sturdy!, consider tanking"
    else:
        return "Low doesn't mean bad, everyone needs a healer!"

