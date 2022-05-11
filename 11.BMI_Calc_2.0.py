print("=================================")
print("Welcome to BMI Calculator")
print("Made with Python")
print("=================================\n")


height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))

# make a result in integer/whole number not float with round function
result = round(weight / (height * height))


print(f'Your height is {height}')
print(f'Your weight is {weight}')
print("================================")
print(f'Your BMI is {result}')

if result < 18.5:
    print("You are underweight!")
elif result <= 25:
    print("You have a normal weight!")
elif result <= 30:
    print("You are slightly overweight!")
elif result <=35:
    print("You're Obese!")
else: 
    print("You're clinically Obese!")