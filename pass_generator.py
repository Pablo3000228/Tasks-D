import random

symbols = '@#$%^&*?!|'
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

password = []
type_of_pass = ['letter'] * 3 + ['num'] * 3 + ['symbol'] * 2

random.shuffle(type_of_pass)

for s in type_of_pass:
    if s == 'letter':
        password.append(random.choice(letters))
    elif s == 'num':
        password.append(str(random.randint(0, 9)))
    else:
        password.append(random.choice(symbols))

print(f"Password: {''.join(password)}")