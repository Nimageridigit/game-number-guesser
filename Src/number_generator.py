import random


def number_generator(min_value=0,max_value=100):
    return random.randint(min_value,max_value)

random_num=number_generator(0,100)