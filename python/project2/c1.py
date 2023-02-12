from prettytable import PrettyTable

name = input("What is your name? ")
location = input("Where are you live? ")
date = input("Date? ")

table = PrettyTable()
table.field_names = ["Name", "Location", "Date"]
table.add_row([name, location, date])

print(table)