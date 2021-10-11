print("Enter a number you'd like to convert: ")
try:
    numb = int(input())
except ValueError:
    print("Invalid data. Enter a natural number or zero")
    quit()
print('''Choose a system you want to convert your number into:
2 ← binary system
8 ← octal system''')
try:
    system = int(input())
except ValueError:
    print("Invalid data. Enter either 2 or 8")
    quit()
if system == 2 and 0 < numb <= 255:
    binary = []
    temp = numb
    while temp > 0:
        binary.append(temp % 2)
        temp = temp // 2
    binary.reverse()
    if numb > 0:
        print(f"In binary system your number equals: {''.join(map(str,binary))}")
        quit()
elif numb == 0:
    print("In binary system your number equals: 0")
elif system == 2 and (numb < 0 or numb > 255):
    print("Invalid data. Enter an integer in range [0;255]")
    quit()
if system == 8:
    octal = []
    temp = numb
    while temp > 0:
        octal.append(temp % 8)
        temp = temp // 8
    octal.reverse()
    if numb > 0:
        print(f"In octal system your number equals: {''.join(map(str, octal))}")
        quit()
    elif numb == 0:
        print("In octal system your number equals: 0")
        quit()
    if numb < 0:
        print("Invalid data. Enter a natural number or zero")
