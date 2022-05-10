print("========================================")
print("Welcome to the Remain Life Calculator")
print("Made with Python")
print("It's just for FUN ;)")
print("========================================")


age = int(input("What is your current age? : "))


'''
1. There are 365 days in a year
2. There are 52 weeks in a year
3. There are 12 months in a year 
'''
fix_num = 90
years = fix_num - age
months = years * 12
weeks = years * 52
days = years * 365

# Printing the output
print(f'You have {days} days, {weeks} weeks, and {months} months left.')