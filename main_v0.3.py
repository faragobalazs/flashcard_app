import random
import words
from words import my_dict

print("                     ")
print("|-------------------|")
print("|   FLASHCARD APP   |")
print("|   v0.1.2          |")
print("|-------------------|")
print("                     ")


#--- This is the function for practicing existing words, phrases, verbs etc.
def practicing():
    kill = False
    while kill == False:
        random_key = random.choice(list(my_dict.keys()))
        random_value = my_dict[random_key]

        print(" ") 
        print("---------------------")
        print("---------------------")
        print(" ")
        question = print(f"You Hungarian word is: \n{random_key}")
        print(" ")
        answer = input("What does it mean in German? \n")

        if answer == "exit":
            kill == True
            main_question()
        elif answer == random_value:
            print(" ")
            print(" ")
            print("THAT'S CORRECT.")
            print(" ")
        else:
            print(" ")
            print(" ")
            print(f"THAT'S WRONG. The right answer was: {random_value}")
            print(" ")

#--- This is the function for saving the dictionary
def save_dictionary(dictionary):
    with open("words.py", "w", encoding="utf-8") as f:
        f.write("my_dict = {\n")
        for key, value in dictionary.items():
            f.write(f"'{key}':'{value}',\n")
        f.write("}")

#--- This is the function for registering new words, phrases, verbs etc.
def registering():
    kill = False
    while kill == False:
        print(" ")
        print("---------------------")
        print("---------------------")
        print(" ")
        sub_question = input("What would you like to do? 'new' or 'exit'\n")

        if sub_question == "new":
            print(" ")
            new_key = input("What is the Hungarian word?: \n")
            new_value = input("What is the German meaning?: \n")
            words.my_dict.update({new_key:new_value})
            save_dictionary(words.my_dict)
        else:
            kill == True
            main_question()


#--- This is the main question in the intro about what to do
def main_question():
    print(" ")
    print("---------------------")
    print("---------------------")
    print(" ")
    todo = input("What would you like to do today? 'practice' or 'register' ?\n")
    if todo == "practice":
        practicing()
    else:
        registering()

#--- Starting functions
main_question()