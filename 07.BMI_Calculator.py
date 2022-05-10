print("=================================")
print("Welcome to BMI Calculator")
print("Made with Python")
print("=================================\n")


height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))

# make a result in integer not float with round function
result = round(weight / (height * height))

print(f'Your height is ' + str(height))
print(f'Your weight is ' + str(weight))
print("================================")
print(f'Your BMI is ' + str(result))