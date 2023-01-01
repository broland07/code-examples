print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? ")) # under 120 cm, you can't
age = int(input("How old are you? ")) # age for ticket price
bill = 0

if height >= 120:
  print("Your height is acceptable for the rollercoaster!")
  if age < 12:
    bill = 7
    print("Ticket for children, $7.")
  elif age <= 18:
    bill = 10
    print("Ticket for teens, $10.")
  elif age >= 45 and age <= 55:
    bill = 12
    print("Retired tickets are $12.")
  else:
    bill = 25
    print("Ticket for adults, $25.")

  w_photo = input("Do you want a photo taken? Y or N. ")
  if w_photo == "Y":
    bill += 3

  print(f"Your final bill is, ${bill}!")

else:
  print("Sorry, you have to grow taller before you can ride!")