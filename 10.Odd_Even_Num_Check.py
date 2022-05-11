print("==================================")
print("Welcome to the Odd Even Number Checker!")
print("Made with Python")
print("==================================")

number = int(input("Which number do you want to check? "))

'''
    Modulo or '%' is operator to calculate how many remainder on number.
    Example: 4 % 2 = 0 ---> (this is an even number)
              3 % 2 = 1 ---> (1 is remainder, it's an odd number)
'''
if number % 2 == 0:
  print("It's an even number!")
else:
  print("It's an odd number!")