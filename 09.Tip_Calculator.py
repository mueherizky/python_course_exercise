print("==================================")
print("Welcome to the tip calculator!")
print("Made with Python")
print("==================================")

total_bill = float(input('What was the total bill? $' ))
given_tip = int(input('How much top would you like to give? 10, 12, or 15 in percentage? : '))
people = int(input('How many people to split the bill? : '))

# to make given_tip to percentage
percentage_given_tip = given_tip / 100

# to know how much tip will pay based on percentage tip
tip = total_bill * percentage_given_tip

# final bill 
final_bill = total_bill + tip

# splitting final bill with many people
split = final_bill / people


'''
to round n decimal places if it contains zero like price,
example $12.00
we must use ":.<n>f"
n is how many decimal what do you print. 
like this, :.2f will print 2 decimal after number.
32 ---> 32.00
14.2 --> 14.20

We can use:
1. print f string             ---> print(f'{39.54484700000000:.2f}') will result "39.54"
2. or print formatting string ---> print("{:.2f}".format(39.54484700000000)) will result same too
'''
print(f'Each person should pay ${split:.2f}')
