import random
from words import my_dict

print("-------------------------------------------------------------------------")
print("|                            FLASHCARD APP                              |")
print("|                                 v0.1                                  |")
print("-------------------------------------------------------------------------")



while 1 < 2:
    random_key = random.choice(list(my_dict.keys()))
    random_value = my_dict[random_key]
    
    print(" ")
    question = print(f"You Hungarian word is: \n{random_key}")
    print(" ")
    answer = input("What does it mean in German? \n")

    if answer == random_value:
        print(" ")
        print("********** THAT'S CORRECT. **********")
    else:
        print(" ")
        print("********** THAT'S WRONG. **********")
        print(f"The right answer was: {random_value}")



