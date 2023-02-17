print("Welcome to the world most popular pizza shop \n")

size = input("select your pizze size - s, m, l \n=")
peperrony = input("do you need peperrony - y or n \n=")
pepsi = input("do you need pepsi bottle - s or l \n=")

bill = 0

if size == "s":
    bill += 50
elif size == "m":
    bill += 70
elif size == "l":
    bill +=  100
else:
    print("The size you selected is wrong. please select s, m, or l ")

if peperrony == "y":
    bill += 5
elif peperrony == "n":
    bill += 0
else:
    print("The size you selected is wrong. please select y, or n ")
    
if pepsi == "s":
    bill += 20
elif pepsi == "l":
    bill += 35
else:
    print("The size you selected is wrong. please select s, or l ")


print(f"your total bill is ${bill}.")
