import math

def paint_calc(height, width, cover):
    cans = (height * width) / 5
    number_of_cans = math.ceil(cans)
    print(f"You'll need {number_of_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

