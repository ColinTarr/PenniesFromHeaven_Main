from math import remainder

amountOfHundreds=0
amountOfFiftys=0
amountOfTens=0
amountOfFives=0
amountOfOnes=0
amountOfQuarters=0
amountOfDimes=0
amountOfNickles=0
NewAmountOfPennies=0

raw_amountOfPennies = input("Inset your desired amount of money here: ")
amountOfPennies = int(raw_amountOfPennies)
 
#100
while amountOfPennies >= 10000:
    amountOfHundreds = amountOfHundreds + 1
    amountOfPennies = amountOfPennies - 10000

#50
while amountOfPennies >= 5000:
    amountOfFiftys = amountOfFiftys + 1
    amountOfPennies = amountOfPennies - 5000
    
#10
while amountOfPennies >= 1000:
    amountOfTens = amountOfTens + 1
    amountOfPennies = amountOfPennies - 1000

#5
while amountOfPennies >= 500:
    amountOfFives = amountOfFives + 1
    amountOfPennies = amountOfPennies - 5000

#1
while amountOfPennies >= 100:
    amountOfOnes = amountOfOnes + 1
    amountOfPennies = amountOfPennies - 100

#.25
while amountOfPennies >= 25:
    amountOfQuarters = amountOfQuarters + 1
    amountOfPennies = amountOfPennies - 25

#.10
while amountOfPennies >= 10:
    amountOfDimes = amountOfDimes + 1
    amountOfPennies = amountOfPennies - 10

#.05
while amountOfPennies >= 5:
    amountOfNickles = amountOfNickles + 1
    amountOfPennies = amountOfPennies - 5

print(f"Total Amount Of Hundred Dollar Bills: {amountOfHundreds}")
print(f"Total Amount Of Fifty Dollar Bills: {amountOfFiftys}")
print(f"Total Amount Of Ten Dollar Bills: {amountOfTens}")
print(f"Total Amount Of Five Dollar Bills: {amountOfFives}")
print(f"Total Amount Of One Dollar Bills: {amountOfOnes}")
print(f"Total Amount Of Quarters: {amountOfQuarters}")
print(f"Total Amount Of Dimes: {amountOfDimes}")
print(f"Total Amount Of Nickles: {amountOfNickles}")
print(f"Total Amount Of Pennies: {amountOfPennies}")