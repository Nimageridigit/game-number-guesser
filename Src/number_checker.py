import random

def number_generator(min_value=0,max_value=100):
    return random.randint(min_value,max_value)

random_num=number_generator(0,100)

try:
    user_number=int(input("Please enter a number between 0 and 100:"))
    if 0 <= user_number <= 100:
        if random_num == user_number:
            print(
            """
            -----------------
            YOU WIN!!!!
            -----------------
            """
            )
        else:
            # TODO

    else:
        print("Your number should be between 0 and 100")
        


except: