import string
import random

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"keys: {key}")

#encrypt

plain_text = input("Print what you want to escrypt: ")
chairs_text = ""
     
for letter in plain_text:
    index = chars.index(letter)
    chairs_text += key[index]

print(chairs_text)