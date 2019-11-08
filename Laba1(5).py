alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
alphabetua = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюяабвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
number = "12345678901234567890"

encrypt = input("Enter e clear message: ")
key = 1
encrypt = encrypt.lower()
encrypted = ""

for letter in encrypt:
    position = alphabet.find(letter)
    newPosition = position + key
    if letter in alphabet:
        encrypted = encrypted + alphabet[newPosition]
    else:
        encryted = encrypted + letter


for letter in encrypt:
    position = alphabetua.find(letter)
    newPosition = position + key
    if letter in alphabetua:
        encrypted = encrypted + alphabetua[newPosition]
    else:
        encryted = encrypted + letter


for letter in encrypt:
    position = number.find(letter)
    newPosition = position + key
    if letter in number:
        encrypted = encrypted + number[newPosition]
    else:
        encryted = encrypted + letter
print("Your cipher is: ", encrypted)