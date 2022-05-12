import random

names_string = input("Give me everybody's names, separated by a comma. \n: ")

'''
    split function is convert string to list based on separator
    below, the separator is comma (,) plus space ( ) for output with space
'''
names = names_string.split(", ")

# to make sure length of "names" list
len_name = len(names)

'''
    why use "len_name - 1" ???
    remember, index in python start with 0 and ended with n - 1
'''
random_pick = random.randint(0, len_name - 1)
person = names[random_pick]
'''
    we can use like this too, very simple. using choice function of random module
    ---> person = random.choice(names)
'''

# to make sure length of "names" list
len_name = len(names)

'''
    why use len_name - 1?
    remember, index in python start with 0 and ended with n-1
'''
random_pick = random.randint(0, len_name - 1)
person = names[random_pick]

print(f'{person} is going to buy the meal today!')