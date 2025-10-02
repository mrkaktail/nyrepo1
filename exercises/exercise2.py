#put in a number
numberinput = int(input("hello! Please write any number: "))
if numberinput > 0:
    print("you chose a positive number")
if numberinput < 0:
    print("you choose a negative number")
if numberinput == 0:
    print("yu choose the number zero")
numberinput2 = int(input("please put in one number"))
numberinput3 = int(input("put in another number"))
if numberinput2 > numberinput3:
    print(f"{numberinput2} is bigger than {numberinput3}")
else: 
    print(f"{numberinput3} is bigger than {numberinput2}")

weight = int(input("please eneter your weight"))
age = int(input("please enter your age"))
amountofpills = int()
if age < 3 and weight < 15:
    print("you get no pills")
if age >= 3 and age <= 7 and weight >= 15 and weight <= 25:
    print("1/2 pills") 
if age >= 7 and age <= 12 and weight >= 26 and weight <= 40:
    print("1/2-1 pills")
if age > 12 and weight > 40:
    print("1-2 pills")
number = int(input("put in any number"))
if number % 2 == 0:
    print("even number")
if number % 2 != 0: 
    print("odd number")
if number % 5 == 0: 
    print("number divisible by 5")
if number % 5 == 0 and number % 2 != 0:
    print("number both odd and is ivisible by 5")
