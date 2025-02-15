# import random
#
# print(random.randint(1,10))
from email.policy import default
from random import randint, choice as get_random_element
import utils.calculator as calc
from utils.templates import Person
from termcolor import cprint
from decouple import config

print(randint(2, 5))
print(get_random_element([7, 8, 9]))

print(calc.multiplication(2, 5))

me = Person('Bob', 25)
print(me)

cprint("Hello, World!", "green", "on_red")

print(config('FILE_PATH'))
print(config('DATABASE_URL'))
commented = config('COMMENTED', default=0, cast=int)
print(commented*2)
