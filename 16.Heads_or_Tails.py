#### Make Program to pick side of coin (HEADS or TAILS) ####

'''
    import is function to import or use a module
    module is another python file with some function for different purpose
'''
import random

'''
    0 is starting point, 1 is end point 
    so it will pick number from 0 to 1 (0-1)

    randint function is a whole number or integer or real number
    random function is float data type ---> random_float = random.random()
'''
random_num = random.randint(0,1)

if random_num == 0:
  print(f'{random_num} is "Tails"')
else:
  print(f'{random_num} is "Heads"')