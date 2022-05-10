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

print(f'Each person should pay ${split:.2f}')
