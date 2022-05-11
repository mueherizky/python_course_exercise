
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1 + name2

# because everyone can type with any case, we must convert it to lower case first
lower_name = combined_name.lower()

t = lower_name.count("t")
r =lower_name.count("r")
u =lower_name.count("u")
e =lower_name.count("e")
true = t + r + u + e

l =lower_name.count("l")
o =lower_name.count("o")
v =lower_name.count("v")
e =lower_name.count("e")
love = l + o + v + e

'''
    Because return of count is integer,
    we must convert it to string first for getting a real number from per word count "true" and "love"
    and then we need convert it to integer, because we need it for logical operation
'''
result = int(str(true) + str(love))

# Conditional Statement
if result < 10 or result > 90:
  print(f'Your score is {result}, you go together like coke and mentos')
elif result > 40 and result < 50:
  print(f'Your score is {result}, your are alright together')
else:
  print(f'Your score is {result}')
        
