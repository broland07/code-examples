alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift_amount, which_direction):
  plain_text = ""
  for letter in text:
    position = alphabet.index(letter)
    if which_direction == "encode":
      new_position = position + shift_amount
    elif which_direction == "decode":
      new_position = position - shift_amount
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")



if direction == "encode":
  caesar(text=text, shift_amount=shift ,which_direction=direction)
elif direction == "decode":
  caesar(text=text, shift_amount=shift ,which_direction=direction)
