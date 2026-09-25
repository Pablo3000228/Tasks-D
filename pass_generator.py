import random

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
specials = "!@#$%^&*"

password = []

for i in range(3):
    password.append(random.choice(letters))

for i in range(3):
    password.append(random.choice(digits))

for i in range(2):
    password.append(random.choice(specials))

random.shuffle(password)

print("Пароль:", ''.join(password))