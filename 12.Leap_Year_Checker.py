print("==================================")
print("Welcome to the Leap Year Checker")
print("Made with Python")
print("==================================")

year = int(input("Which year you want to check? : "))


'''
If year cleanly divide by 4, "Leap Year"
If year cleanly divide by 100, "Not Leap Year"
If year cleanly divide by 400, "Leap Year"

Flowchart Algorithm ---> https://bit.ly/36BjS2D
'''
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap Year!")
    else: 
      print("Not Leap Year!")
  else:
    print("Leap Year!")
else:
  print("Not Leap Year!")