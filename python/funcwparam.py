def greet():
  print("Hello!")
  print("How do you do?")

greet()

def greet_w_name(name):
  print(f"Hello, {name}!")
  print(f"How do you do, {name}?")

greet_w_name("Jack")

def greet_w(name, location):
  print(f"Hi! My name is {name}, and i'm from {location}.")

greet_w("Jack", "LA")

greet_w(location="LA", name="Jack")