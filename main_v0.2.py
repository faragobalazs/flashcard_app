import random
from words import my_dict

print("                                                                         ")
print("-------------------------------------------------------------------------")
print("|                            FLASHCARD APP                              |")
print("|                               v0.1.1                                  |")
print("-------------------------------------------------------------------------")
print("                                                                         ")


#--- This is the function for practicing existing words, phrases, verbs etc.
def practicing():
    kill = False
    while kill == False:
        random_key = random.choice(list(my_dict.keys()))
        random_value = my_dict[random_key]
        
        print("-------------------------------------------------------------------------")
        question = print(f"You Hungarian word is: \n{random_key}")
        print(" ")
        answer = input("What does it mean in German? \n")

        if answer == "exit":
            kill == True
            main_question()
        elif answer == random_value:
            print(" ")
            print("THAT'S CORRECT.")
            print(" ")
        else:
            print(" ")
            print("THAT'S WRONG.")
            print(f"The right answer was: {random_value}")
            print(" ")


#--- This is the function for registering new words, phrases, verbs etc.
def registering():
    pass


#--- This is the main question in the intro about what to do
def main_question():
    print(" ")
    print("-------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------")
    todo = input("What would you like to do today? 'practice' or 'register' ?\n")
    if todo == "practice":
        practicing()
    else:
        registering()

#--- Starting functions
main_question()