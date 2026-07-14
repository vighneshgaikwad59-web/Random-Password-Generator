import random

chars = ("13233eddt443ewder")
core = int(input("Enter your value "))
password = ""

for a in range(core):
    password += random.choice(chars)

print(password)
