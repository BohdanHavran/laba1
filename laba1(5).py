alphabet = "abcdefghijklmnopqrstuvwxyzaабвгґдеєжзиіїйклмнопрстуфхцчшщьюяа12345678901"

while True:
    encrypt = input("Enter text: ")
    key = 1
    encrypt = encrypt.lower()
    encrypted = ""


    for letter in encrypt:
        position = alphabet.find(letter)
        newPosition = position + key
        if letter in alphabet:
            encrypted = encrypted + alphabet[newPosition]
        else:
            encrypted = encrypted +letter
    print("Your cipher is: ",encrypted)
