# with open("file.txt") as file:
#     content = file.read()
#     print(content)

with open("file.txt", mode="a") as file:
    file.write("\nSecond line from script.")
#    print(content)


# file = open("file.txt")
# content = file.read()
# print(content)

# file.close()