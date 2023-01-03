import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

index = random.randint(0,len(names)-1)
winner = names[index]

print(f"{winner} is going to buy the meal today!")