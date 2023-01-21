import os

dict = {}
end = False

while not end:
    key = input("Key: ")
    value = input("Value: ")
    dict[key] = value
    end_of = input("Do you wanna add new value? Yes/No: ")
    if end_of == "Yes" or end_of == "yes":
        os.system('clear')
    elif end_of == "No" or end_of == "no":
        end = True

os.system('clear')
for elements in dict:
    get_value = dict[elements]
    print(f"The key is: {elements}, and the value is: {get_value}.")