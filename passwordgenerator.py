import random

sletters = "abcdefghijklmnopqrstuvwxyz"
bletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"
special = "!@#$%^&*()_+=-[]{}|\';:?/><.,`~"
ans = "y"


def passgen():
    password = ""
    length = int(input("Enter len of password: "))
    for i in range(length):
        x = random.randint(1,4)
        if x == 1:
            password += sletters[random.randint(0,25)]
        if x == 2:
            password += bletters[random.randint(0,25)]
        if x == 3:
            password += num[random.randint(0,9)]
        if x == 4:
            password += special[random.randint(0,29)]
    return password

while ans.lower() == "y":
    print(passgen())
    ans = input("Want some more tables? (y/n): ")

print("Thankyou")