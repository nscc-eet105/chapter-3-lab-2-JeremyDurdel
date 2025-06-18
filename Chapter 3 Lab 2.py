print ("Jeremy's Stuff Store")
print()

Number_of_Items = int(input("How many items would "
                            "you like to purchase? "))
total = 0
print()
for num in range(1, Number_of_Items + 1):
    Cost = float(input(f"Enter the price of item {num}: "))
    total += Cost
    print()
#Sets loop for price inputs

print()
print(f'The total cost of your items is ${total:,.2f}.')
#Calculates and prints total cost

print()
Average_Cost = total / num
print(f'The average cost of each item is ${Average_Cost:,.2f}')
#Calculates and prints average cost

#Jeremy Durdel
#Chapter 3 Lab 2
#06/17/2025
