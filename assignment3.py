
# 1. Nested Decisions: The Adventure Game 🏰
# Objective:

# To practice the use of nested if statements in creating a simple text-based adventure game.

# Task 1: Code Correction

# You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them.

# Buggy Code:


# place = input("Choose a place: forest or cave? ")
# if place = "forest":
#     action = input("climb a tree or cross a river?")
#     if action = "climb a tree":
#         print("You found a bird's nest!")
#     else action = "cross a river":
#         print("You found a boat!")
# elif place = "cave":
#     print("You find a hidden treasure!")
# Task 2: Setting the Scene

# Based on the corrected code from Task 1, expand the game. If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.

# Task 3: Default Path

# If the user makes an invalid choice at any point, use the pass statement for now. Later, you can enhance this to provide feedback or a different branch of the story.

place = input("Choose a place: forest or cave? ")
if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        print('''
now you are in a zombie apocalypse and you also dont have clothes 
tip: there is a trafic sign that says "nearby to Rosewood" it's sounds like a good place to start
stay silent..''')
elif place == "cave":
    print("You find a hidden treasure!")
    action=input("Now you are in a dark cave: light a torch or proceed in the dark: ")
    if action=="proceed in the dark":
        print("sound like if someone is tearing meat but you walks in the dark and comes out from the cave safely afther of that you lived a plenty life")
    elif action=="light a torch":
        print('''
When you turn on the torch you discover that's not a cave, it's a spider's nest, now RUN!
You runned the fastest that you can but the gigant spiders catch you
You died
              ''')
    else:
        print("Boo! You died due a cardiovascular accident")
else:
    print("Well, you didn't pick correctly so i will pick for you, now you are in the middle of the ocean")
    action=input("You see a pirate ship: swim far from the ship or try if they pick you up: ")
    if action=="try if they pick you up":
        print("They give you some ron and goes to the nearest island for more party")
    else:
        print("You got drowned")

print('''
-----------------------------------
i wish you liked that little story!
-----------------------------------
''')
# 2. Quick Decisions: The Event Planner 🎉
# Objective:

# To practice the use of shorthand if statements in determining event-related decisions.

# Task 1: Code Correction

# You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

# Buggy Code:

# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 else "conference room"
# print(venue)
# Task 2: Venue Selection
# Based on the corrected code from Task 1, further enhance the program to recommend additional facilities like "audio system" or "projector" based on the number of attendees.
try:
    attendees = int(input("Enter number of attendees: "))

    venue = "conference room" if attendees < 100 else "large hall"
    print(venue)
    if attendees >120:
        print("install the audio sistem")
        condition=input("There is any kid?: yes/no ")
        if condition=="yes":
            print("Use the play room")
        else:
            print("Waiters and alcohol service")   
    elif attendees>150:
        print("We are going to need the projector")
    elif attendees<20:
        print("Service of taxi")   
except ValueError:
    pass
DIVIDER=('''
----------------------------------------------------------------
                       Exercise divider
----------------------------------------------------------------
      
''')
print(DIVIDER)
# Task 3: Catering Choices

# Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".
food="Veggie Delight Caterers" if input("Hello sir, do you want vegetarian food? ")=="yes i will like it" else print("Perfect!, We have the Gourmet Meals Caterers that's our speciality")
if food=="Veggie Delight Caterers":
    print("Yes sir, whe have the Veggie Delight Caterers")
print(DIVIDER)
# 3. Silent Failures: The Error Handler 🐞
# Objective:

# To practice the use of the pass statement in handling potential errors silently.

# Task 1: Code Correction

# You are provided with a Python script that is supposed to handle errors silently, but it has some mistakes. Identify and fix them.

# Buggy Code:
# Task 2: Division Calculator

# Based on the corrected code from Task 1, enhance the program to handle other potential errors, such as a ValueError or TypeError. Experiment with what happens when you divide an integer by a string and identify what kind of error it gives you. Then use the except statement to handle the error.


try:
 x = 1 / 0
except ZeroDivisionError:
    pass
except TypeError:
    pass

try:
    car="Honda"
    car+=1
except TypeError:
    pass

# Task 3: File Reader

# Ask the user for a filename to read. Try to open and read the file. If the file doesn't exist, use the pass statement to handle the error silently.
try:
    file=input("Please introduce the name of the file that are you trying to open: ")
    f = open(file, "r")
    print(f.read())
except FileNotFoundError:
    f = open("test.txt", "r")
    print(f.read())
print(DIVIDER)
# 4. Nested Quick Decisions: The Shopping Assistant 🛍️
# Objective:

# To practice the use of nested shorthand if statements in assisting a shopping decision.

# Task 1: Code Correction

# You are provided with a Python script that is supposed to assist in shopping, but it has errors. Identify and fix them.

# Buggy Code:

# weather = input("Enter the weather: sunny, rainy, or cold: ")
# clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater"
# print(clothing)
# Task 2: Clothing Recommendation
# Task 2: Clothing Recommendation
# Based on the corrected code from Task 1, further enhance the program to recommend additional items like "hat" or "boots" based on the weather.

# Task 3: Accessory Recommendation

# Based on the clothing recommendation, suggest an accessory. For instance, if "sunglasses" were recommended, suggest "sunscreen" as an accessory.

weather = input("Enter the weather: sunny, rainy, or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater"
print(clothing)
if clothing=="sunglasses":
    print("I would recommend to use solar protection!")
hard_weather=input("there is a extreme weather? yes:no? ")
if hard_weather=="yes":
    specialclothing=input('''what type of hard clima is it?
                            1-Tornado 2-hailing 3-Snow storm
                            ''')
    if specialclothing=="1":
        print("I hope that you dont have to go outside, try ussing a hat and tought clothes")
    if specialclothing=="2":
        print("Use a hat")
    if specialclothing=="3":
        print("Use snow bots!")
else:
    print("I think you are going to be okay with these clothes")
print(DIVIDER)
# 5. The Silent Logger: System Monitor 🖥️
# Objective:

# To practice the use of the pass statement in a system monitoring context.

# Task 1: Code Correction

# You are provided with a Python script that is supposed to monitor system parameters, but it has some mistakes. Identify and fix them.

# Buggy Code:


# import random
# cpu_usage = random.randint(0, 100)
# if cpu_usage > 90:
#     print("High CPU usage!")
# elif cpu_usage > 80 and cpu_usage <= 90
#     pass
# Task 2: System Check

# Based on the corrected code from Task 1, enhance the program to also monitor memory usage and disk space, and provide alerts accordingly.

import random
cpu_usage = random.randint(0, 100)
disk_usage=random.randint(0,100)
ram_usage=random.randint(0,100)
if cpu_usage > 90:
    print("High CPU usage!")
    user_decition=input("Do you want to restart the PC? Yes/No :")
    if user_decition=="yes":
        print("restarting")  
if disk_usage>90:
    print("High disk usage it could make your pc slower")
if ram_usage>90:
    ("print high ram usage")
if ram_usage>90 and disk_usage>90 and cpu_usage>90:
    user_decition2=input("Your pc is on a critical state, do you want to format the computer? yes/no ")
    if user_decition=="yes":
        print("it would take a few minutes") 
elif ram_usage<30 and disk_usage<30 and cpu_usage<30:
    print("Your pc is on optimal state")
    
 



